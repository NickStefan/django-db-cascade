from django.db.backends.postgresql_psycopg2.schema import DatabaseSchemaEditor as DSE

class DatabaseSchemaEditor(DSE):
    sql_create_fk = (
        "ALTER TABLE %(table)s ADD CONSTRAINT %(name)s FOREIGN KEY (%(column)s) "
        "REFERENCES %(to_table)s (%(to_column)s)%(cascade)s%(deferrable)s"
    )

