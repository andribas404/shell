import datetime
import logging
import pandas as pd

from peewee import *

DATABASE_FILENAME = 'shell.db'
database = SqliteDatabase(DATABASE_FILENAME, pragmas={'foreign_keys': 1})

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
        field_data = dict(self._data)
        current_version = field_data.pop('version', 1)
        field_data = self._prune_fields(field_data, self.dirty_fields)
        if not field_data:
            raise ValueError('No changes have been made.')

        ModelClass = type(self)
        field_data['version'] = ModelClass.version + 1  # Atomic increment.

        query = ModelClass.update(**field_data).where(
            (ModelClass.version == current_version) &
            (ModelClass.id == self.id))
        if query.execute() == 0:
            # No rows were updated, indicating another process has saved
            # a new version. How you handle this situation is up to you,
            # but for simplicity I'm just raising an exception.
            raise ConflictDetectedException()
        else:
            # Increment local version to match what is now in the db.
            self.version += 1
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

    class Meta:
        indexes = (
            # create a unique on name, birthday
            (('first_name', 'second_name', 'last_name', 'birthday'), True),
        )

def get_persons():
    data = pd.read_csv('person.csv')
    return data.to_dict('records')

def populate_test_data():
    with database:
        database.drop_tables([Department, Person])
        database.create_tables([Department, Person])

    dpts = [('Бухгалтерия',), ('Отдел автоматизации',), ('Отдел продаж',)]

    with database.atomic():
        Department.insert_many(dpts, fields=[Department.name]).execute()
        Person.insert_many(get_persons()).execute()



# Print all queries to stderr.
logger = logging.getLogger('peewee')
logger.addHandler(logging.StreamHandler())
#logger.setLevel(logging.DEBUG)


#populate_test_data()
d = (Department
    .select()
    .order_by(Department.name))
for dpt in d:
    print(dpt.name)

persons = (Person
    .select(Person.first_name, Person.last_name, Department.name.alias('dpt_name'))
    .join(Department)
    )

for p in persons.dicts().iterator():
    print(p)
