import datetime
import logging
import pandas as pd

from models import database, Person, Department
from models import BaseVersionedModel
from playhouse.shortcuts import model_to_dict, dict_to_model
from peewee import IntegrityError

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

def test_models():
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


class ItemList:
    """Используется для доступа к коллекции элементов
    с помощью REST API"""
    fields = 'first_name second_name last_name birthday sex position dpt is_archive'.split()

    @staticmethod
    def list():
        """возврашает список всех элементов в виде именованного кортежа"""
        return list(Person.select().namedtuples().iterator())
    
    @staticmethod
    def create(item):
        """добавляет в коллекцию новый элемент.
        элемент приходит в виде словаря
        во время вставки делает блокировку на запись"""
        try:
            d = {key:item[key] for key in ItemList.fields if key in item}
            return Person.insert(**d).execute()
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
            return p.save_optimistic()
        except Person.DoesNotExist as err:
            raise IndexError('Элемента с данным ID нет')
        except IntegrityError as err:
            raise err
        except BaseVersionedModel.OutdatedError as err:
            raise err

def test_list():
    print(ItemList.get(26))
    try:
        print(ItemList.get(100))
    except IndexError as err:
        print(err)

    #ItemList.delete(26)

    person_row = 'Иванов,Иван,Иванович,1997-08-30,М,Программист,2,True'.split(',')
    person_dict = {k:v for k,v in zip(ItemList.fields, person_row)}
    print(person_dict)

    #new_person = ItemList.create(person_dict)
    #print(new_person)