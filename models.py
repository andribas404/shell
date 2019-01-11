import datetime

import asyncio
import peewee
import peewee_async

DATABASE_FILENAME = 'people.db'
database = peewee.SqliteDatabase(DATABASE_FILENAME)

class Person(peewee.Model):
    name = peewee.CharField()
    birthday = peewee.DateField()

    class Meta:
        database = database # This model uses the "people.db" database.

# simple utility function to create tables
def create_tables():
    with database:
        database.create_tables([Person])

