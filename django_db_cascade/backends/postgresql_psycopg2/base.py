from django.db.backends.postgresql_psycopg2.base import DatabaseWrapper as DBW
from django_db_cascade.backends.postgresql_psycopg2 import DataBaseSchemaEditor

class DatabaseWrapper(DBW):
    SchemaEditorClass = DatabaseSchemaEditor

