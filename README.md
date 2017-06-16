# django-db-cascade

### Installation
`pip install django-db-cascade`

settings.py:
```
DATABASES = {
    'default': {
        'ENGINE': 'django_db_cascade.backends.postgresql_psycopg2',
        # ... etc ...
    }
}
```

### Usage
```
from django.db import models
from django_db_cascade.fields import ForeignKey
from django_db_cascade.deletions import DB_CASCADE

class Thing(Common):
    account = ForeignKey('self', DB_CASCADE)
```

# How it works
1. subclassed the postgresql backend
2. subclassed the foreign key field
3. implemented a constant called DB_CASCADE
4. django migration framework recognizes the model field inputs have changed
5. django generates a migration which rewrites the foreign key SQL for the field
6. example SQL generated:
    ```
    ALTER TABLE mytable ADD CONSTRAINT myconstraint FOREIGN KEY (mycolumn)
    REFERENCES myothertable myothercolumn ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED
    ```

# Future proof
If, and when, on_cascade_db ever gets into django, editing these generated migrations should be very easy.

Generated migrations:
```
migrations.AlterField(
    model_name='modelname',
    name='fieldname',
    field=django_db_cascade.fields.ForeignKey(on_delete=django_db_cascade.deletions.DB_CASCADE)
)
```

Changing them over, if django ever handles on_delete_db natively, might look like:
```
migrations.AlterField(
    model_name='modelname',
    name='fieldname',
    field=django.db.models.ForeignKey(on_delete=models.DB_CASCADE)
)
```

# Ticket
The ticker where django has discussed bringing on_delete_db to django:
https://code.djangoproject.com/ticket/21961
