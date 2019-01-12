import datetime
import logging
import pandas as pd

from models import database, Person, Department, ItemList
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


def test_list():
    print(ItemList.get(26))
    try:
        print(ItemList.get(100))
    except IndexError as err:
        print(err)

    #ItemList.delete(26)
    fields = 'first_name second_name last_name birthday sex position dpt is_archive'.split()
            
    person_row = 'Иванов,Иван,Иванович,1997-08-30,М,Программист,2,True'.split(',')
    person_dict = {k:v for k,v in zip(fields, person_row)}
    print(person_dict)

    #new_person = ItemList.create(person_dict)
    #print(new_person)