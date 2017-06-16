from django.db.models import (
    ForeignKey as FK, OneToOneField as OTO,
    DO_NOTHING
)
from django_db_cascade.deletions import DB_CASCADE

### in actual django source we could just edit the class ForeignObject

class ForeignKey(FK):
    def __init__(self, to, on_delete, **kwargs):
        if on_delete == DB_CASCADE:
            self.on_delete_db_cascade = True
            on_delete = DO_NOTHING
        else:
            self.on_delete_db_cascade = False
        super(ForeignKey, self).__init__(to, on_delete, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(ForeignKey, self).deconstruct()
        if self.on_delete_db_cascade:
            kwargs['on_delete'] = DB_CASCADE
        return name, path, args, kwargs

class OneToOneField(OTO):
    def __init__(self, to, on_delete, **kwargs):
        if on_delete == DB_CASCADE:
            self.on_delete_db_cascade = True
            on_delete = DO_NOTHING
        else:
            self.on_delete_db_cascade = False
        super(OneToOneField, self).__init__(to, on_delete, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(OneToOneField, self).deconstruct()
        if self.on_delete_db_cascade:
            kwargs['on_delete'] = DB_CASCADE
        return name, path, args, kwargs

