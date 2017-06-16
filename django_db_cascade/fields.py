from django.db.models import ForeignKey as FK
from django_db_cascade.deletions import DB_CASCADE

class ForeignKey(FK):
    def __init__(self, to, on_delete, **kwargs):
        self.on_delete_db_cascade = True if on_delete == DB_CASCADE else False
        super().__init__(to, on_delete, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(ForeignKey, self).deconstruct()
        if self.on_delete_db_cascade:
            kwargs['on_delete'] = DB_CASCADE
        return name, path, args, kwargs
