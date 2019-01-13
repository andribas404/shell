import datetime
import logging

from peewee import SqliteDatabase, Model, IntegrityError
from peewee import CharField, IntegerField, DateField, ForeignKeyField, BooleanField
from playhouse.shortcuts import model_to_dict, dict_to_model

DATABASE_FILENAME = 'shell.db'
database = SqliteDatabase(DATABASE_FILENAME, pragmas={'foreign_keys': 1})

class OutdatedError(Exception):
    """Класс ошибки, когда происходит попытка перезаписать уже изменившуюся запись"""
    pass

class BaseVersionedModel(Model):
    """Базовая модель для данных. указывает используемую БД
    и использует оптимистическую блокировку
    http://docs.peewee-orm.com/en/latest/peewee/hacks.html#optimistic-locking"""

    version = IntegerField(default=1, index=True)

    def save_optimistic(self):
        if not self.id:
            # This is a new record, so the default logic is to perform an
            # INSERT. Ideally your model would also have a unique
            # constraint that made it impossible for two INSERTs to happen
            # at the same time.
            return self.save()

        # Update any data that has changed and bump the version counter.
        field_data = dict(self.__data__)
        current_version = field_data.pop('version', 1)
        field_data = self._prune_fields(field_data, self.dirty_fields)

        if not field_data:
            return True

        ModelClass = type(self)
        field_data['version'] = ModelClass.version + 1  # Atomic increment.

        query = ModelClass.update(**field_data).where(
            (ModelClass.version == current_version) &
            (ModelClass.id == self.id))
        if query.execute() == 0:
            # No rows were updated, indicating another process has saved
            # a new version. How you handle this situation is up to you,
            # but for simplicity I'm just raising an exception.
            raise OutdatedError()
        else:
            # Increment local version to match what is now in the db.
            self.version = int(self.version) + 1
            return True

    class Meta:
        database = database


class Department(BaseVersionedModel):
    """Модель подразделений предприятия
    Поля: 
    name - название отдела
    """
    #название отдела 
    name = CharField(unique=True)

    def __str__(self):
        return 'Department: {}'.format(self.name)

class Person(BaseVersionedModel):
    """Модель сотрудников предприятия
    Поля: 
    first_name - Имя
    second_name - Отчество
    last_name - Фамилия
    birthday - Дата рождения
    sex - Пол
    position - Должность
    dpt - Отдел
    is_archive - Находится ли в архиве
    """

    #ФИО 
    first_name = CharField()
    second_name = CharField()
    last_name = CharField()
    
    #дата рождения 
    birthday = DateField()

    MALE = ('М', 'Мужской')
    FEMALE = ('Ж', 'Женский')

    SEX_CHOICES = [MALE, FEMALE]
    #пол
    sex =  CharField(choices=SEX_CHOICES)

    #должность
    position = CharField()
    
    #отдел
    dpt = ForeignKeyField(Department, backref='persons')

    #дело в архиве
    is_archive = BooleanField(default=False)

    @property
    def name(self):
        return ' '.join((self.first_name, self.last_name))
    
    def __str__(self):
        return 'Person: {name} at position {position}'.format(name=self.name, position=self.position)

    class Meta:
        indexes = (
            # create a unique on name, birthday
            (('first_name', 'second_name', 'last_name', 'birthday'), True),
        )


class ItemList:
    """Используется для доступа к коллекции элементов
    с помощью REST API"""
    @staticmethod
    def get_index():
        """возврашает список всех элементов"""
        return list(Person.select().dicts().iterator())
    
    @staticmethod
    def get_dpt():
        """возврашает список всех отделов"""
        return list(Department.select().dicts().iterator())

    @staticmethod
    def create(item):
        """добавляет в коллекцию новый элемент.
        элемент приходит в виде словаря"""
        try:
            fields = 'first_name second_name last_name birthday sex position dpt is_archive'.split()
            d = {key:item[key] for key in fields if key in item}
            p = Person.create(**d)
            return model_to_dict(p)
        except IntegrityError as err:
            raise err

    @staticmethod
    def get(id):
        """возвращает элемент по id в виде словаря"""
        try:
            return model_to_dict(Person.get_by_id(id))
        except Person.DoesNotExist as err:
            raise IndexError('Элемента с данным ID нет')
    
    @staticmethod
    def delete(id):
        """удаляет элемент по id"""
        try:
            p = Person.get_by_id(id)
            return p.delete_instance()
        except Person.DoesNotExist as err:
            raise IndexError('Элемента с данным ID нет')

    @staticmethod
    def update(id, item):
        """обновляет значение полей элемента с заданным id"""
        try:
            p = Person.get_by_id(id)
            for key,v in item.items():
                if getattr(p, key) != v: 
                    setattr(p, key, v)
            if not p.save_optimistic():
                raise IntegrityError()
            return model_to_dict(p)
        except Person.DoesNotExist as err:
            raise IndexError('Элемента с данным ID нет')
        except IntegrityError as err:
            raise err
        except OutdatedError as err:
            raise err