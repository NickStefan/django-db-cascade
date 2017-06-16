from django.db.backends.postgresql_psycopg2.schema import DatabaseSchemaEditor as DSE

class DatabaseSchemaEditor(DSE):

    sql_on_delete_cascade = " ON DELETE CASCADE "

    sql_create_fk = (
        "ALTER TABLE %(table)s ADD CONSTRAINT %(name)s FOREIGN KEY (%(column)s) "
        "REFERENCES %(to_table)s (%(to_column)s)%(on_delete)s%(deferrable)s"
    )

    def _create_on_delete_sql(self, model, field, suffix):
        on_delete_db_cascade = getattr(field, "on_delete_db_cascade", False)
        if on_delete_db_cascade:
            return self.sql_on_delete_cascade
        else:
            return ""

    def _create_fk_sql(self, model, field, suffix):
        from_table = model._meta.db_table
        from_column = field.column
        to_table = field.target_field.model._meta.db_table
        to_column = field.target_field.column
        suffix = suffix % {
            "to_table": to_table,
            "to_column": to_column,
        }

        return self.sql_create_fk % {
            "table": self.quote_name(from_table),
            "name": self.quote_name(self._create_index_name(model, [from_column], suffix=suffix)),
            "column": self.quote_name(from_column),
            "to_table": self.quote_name(to_table),
            "to_column": self.quote_name(to_column),
            "deferrable": self.connection.ops.deferrable_sql(),
            "on_delete": self._create_on_delete_sql(model, field, suffix)
        }
