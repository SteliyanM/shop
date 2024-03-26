from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser

from django.db import models


class BokataStoreUser(AbstractBaseUser):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    phone_number = models.CharField(
        max_length=
    )

