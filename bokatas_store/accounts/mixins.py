from django.contrib.auth import get_user_model
from django.db import models


class UserField(models.Model):
    class Meta:
        abstract = True

    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        primary_key=True,
    )