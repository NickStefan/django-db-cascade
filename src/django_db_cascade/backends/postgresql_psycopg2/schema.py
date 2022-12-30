from django.db.backends.postgresql_psycopg2.schema import DatabaseSchemaEditor as DSE
from django.db.models import ForeignKey


class DatabaseSchemaEditor(DSE):

    sql_on_delete_cascade = " ON DELETE CASCADE "
    sql_on_delete_set_null = " ON DELETE SET NULL "

    sql_create_fk = (
        "ALTER TABLE %(table)s ADD CONSTRAINT %(name)s FOREIGN KEY (%(column)s) "
        "REFERENCES %(to_table)s (%(to_column)s)%(on_delete)s%(deferrable)s"
    )

    def _create_on_delete_sql(self, model, field, suffix):
        on_delete_db_cascade = getattr(field, "on_delete_db_cascade", False)
        on_delete_db_set_null = getattr(field, "on_delete_db_set_null", False)

        if on_delete_db_cascade:
            return self.sql_on_delete_cascade
        elif on_delete_db_set_null:
            return self.sql_on_delete_set_null
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
            "name": self.quote_name(self._create_index_name(from_table, [from_column], suffix=suffix)),
            "column": self.quote_name(from_column),
            "to_table": self.quote_name(to_table),
            "to_column": self.quote_name(to_column),
            "deferrable": self.connection.ops.deferrable_sql(),
            "on_delete": self._create_on_delete_sql(model, field, suffix)
        }

    def _alter_field(self, model, old_field, new_field, old_type, new_type,
                     old_db_params, new_db_params, strict=False):
        super(DatabaseSchemaEditor, self)._alter_field(model=model, old_field=old_field, new_field=new_field,
                                                       old_type=old_type, new_type=new_type,
                                                       old_db_params=old_db_params, new_db_params=new_db_params,
                                                       strict=strict)

        if new_field.db_constraint and isinstance(new_field, ForeignKey):
            self.execute(self._create_fk_sql(model, new_field, "_fk_%(to_table)s_%(to_column)s"))
