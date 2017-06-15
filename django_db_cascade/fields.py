from django.db.models import ForeignKey as FK

class ForeignKey(FK):
    def __init__(self, *args, db_cascade=False, **kwargs):
        self.db_cascade = db_cascade
        kwargs.pop('db_cascade', None)
        super().__init__(*args, **kwargs)

