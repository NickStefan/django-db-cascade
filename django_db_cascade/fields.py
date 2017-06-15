from django.db.models import ForeignKey as FK

class ForeignKey(FK):
    def __init__(self, to, on_delete, **kwargs):
        db_cascade = kwargs.pop('db_cascade', False)
        self.db_cascade = db_cascade
        super().__init__(to, on_delete, **kwargs)
