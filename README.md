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

### Caveats
- CASCADE_DB only supports Postgres
- CASCADE_DB does not support django on_delete signals
- CASCADE_DB will not cascade delete multiple inherited tables as expected
- CASCADE_DB will not trigger models.CASCADE on another model. E.g. Model A points to model B, via CASCADE_DB. Model B points to model C, via CASCADE. A will cascade delete B, but B will not cascade delete C.

### How it works
1. Minimal subclassing of the django postgresql backend and the django ForeignKey field
3. Added a new possible value for ForeignKey's on_delete kwarg, called CASCADE_DB
4. When you use CASCADE_DB, the migration framework will recognize a change, and write new sql
6. example SQL generated:
    ```
    ALTER TABLE mytable ADD CONSTRAINT myconstraint FOREIGN KEY (mycolumn)
    REFERENCES myothertable myothercolumn ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED
    ```

### Future proof
If, and when, DB_CASCADE ever gets into django, editing these generated migrations should be very easy.

Generated migrations:
```
migrations.AlterField(
    model_name='modelname',
    name='fieldname',
    field=django_db_cascade.fields.ForeignKey(on_delete=django_db_cascade.deletions.DB_CASCADE)
)
```

Changing them over, if django ever handles DB_CASCADE natively, might look like:
```
migrations.AlterField(
    model_name='modelname',
    name='fieldname',
    field=django.db.models.ForeignKey(on_delete=models.DB_CASCADE)
)
```

### Ticket
The ticker where django has discussed bringing DB_CASCADE to django:
https://code.djangoproject.com/ticket/21961
