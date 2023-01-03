from django.db.models import (
    ForeignKey as FK, OneToOneField as OTO,
    DO_NOTHING
)
from .deletions import DB_CASCADE, DB_SET_NULL

### in actual django source we could just edit the class ForeignObject

class ForeignKey(FK):
    def __init__(self, to, on_delete, **kwargs):
        self.on_delete_db_cascade = False
        self.on_delete_db_set_null = False

        if on_delete == DB_CASCADE:
            self.on_delete_db_cascade = True
            on_delete = DO_NOTHING
        elif on_delete == DB_SET_NULL:
            self.on_delete_db_set_null = True
            on_delete = DO_NOTHING

        super(ForeignKey, self).__init__(to, on_delete, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(ForeignKey, self).deconstruct()
        if self.on_delete_db_cascade:
            kwargs['on_delete'] = DB_CASCADE
        elif self.on_delete_db_set_null:
            kwargs['on_delete'] = DB_SET_NULL
        return name, path, args, kwargs

class OneToOneField(OTO):
    def __init__(self, to, on_delete, **kwargs):
        self.on_delete_db_cascade = False
        self.on_delete_db_set_null = False

        if on_delete == DB_CASCADE:
            self.on_delete_db_cascade = True
            on_delete = DO_NOTHING
        elif on_delete == DB_SET_NULL:
            self.on_delete_db_set_null = True
            on_delete = DO_NOTHING

        super(OneToOneField, self).__init__(to, on_delete, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(OneToOneField, self).deconstruct()
        if self.on_delete_db_cascade:
            kwargs['on_delete'] = DB_CASCADE
        elif self.on_delete_db_set_null:
            kwargs['on_delete'] = DB_SET_NULL
        return name, path, args, kwargs

