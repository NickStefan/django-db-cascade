# django-db-cascade-2

### Installation for Django 3
`pip install django-db-cascade-2`

### Installation for Django 2
`pip install django-db-cascade-2==0.2.3`

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
from django_db_cascade.fields import ForeignKey, OneToOneField
from django_db_cascade.deletions import DB_CASCADE

class Thing(Common):
    account = ForeignKey('self', DB_CASCADE)
```

### Caveats
- DB_CASCADE only supports Postgres
- DB_CASCADE does not support django on_delete signals
- DB_CASCADE will not cascade delete multiple inherited tables as expected
- DB_CASCADE will not trigger CASCADE on another model. E.g. Model A points to model B, via DB_CASCADE. Model B points to model C, via CASCADE. A will cascade delete B, B will django delete C, but __deleting A will not delete C__!
- DB_CASCADE on a ManyToMany of A <---> B, only A_B set records will be cascade deleted (deleting A will not delete B)

### How it works
1. Minimal subclassing of the django postgresql backend and the django ForeignKey field
3. Added a new possible value for ForeignKey's on_delete kwarg, called DB_CASCADE
4. When you use DB_CASCADE, the migration framework will recognize a change, and write new sql
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
