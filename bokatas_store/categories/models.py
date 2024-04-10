from django.core.validators import MinLengthValidator
from django.db import models

from bokatas_store.core.model_mixins import SlugFieldMixin


class Category(SlugFieldMixin):
    NAME_MAX_LENGTH = 50
    NAME_MIN_LENGTH = 3

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(
                limit_value=NAME_MIN_LENGTH,
                message=f"{__name__} name must contain at latest {NAME_MIN_LENGTH}",
            ),
        ),
        error_messages={
            "unique": f"{__name__} with that name already exists",
            "max_length": f"{__name__} name must conatain max {NAME_MAX_LENGTH}",
        }
    )

    picture = models.ImageField(
        upload_to="category_pictures",
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name
