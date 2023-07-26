from django.contrib.auth.models import AbstractUser
from django.db.models import CharField


class User(AbstractUser):
    code = CharField(max_length=32, blank=True, null=True)

    class Meta:
        db_table = 'auth_user'
