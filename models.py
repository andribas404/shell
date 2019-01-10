import datetime
import os
import re

from peewee import *

DATABASE_FILENAME = 'people.db'
database = SqliteDatabase(DATABASE_FILENAME)

class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = database # This model uses the "people.db" database.

# simple utility function to create tables
def create_tables():
    with database:
        database.create_tables([Person])

