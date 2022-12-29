from django.db.backends.postgresql_psycopg2.base import DatabaseWrapper as DBW
from .schema import DatabaseSchemaEditor

class DatabaseWrapper(DBW):
    SchemaEditorClass = DatabaseSchemaEditor
