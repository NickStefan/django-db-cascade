from django.db.backends.postgresql.base import DatabaseWrapper as DBW
from .schema import DatabaseSchemaEditor

class DatabaseWrapper(DBW):
    SchemaEditorClass = DatabaseSchemaEditor
