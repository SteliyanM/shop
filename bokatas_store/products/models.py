from django.core.validators import MinLengthValidator
from django.db import models

from core.model_mixins import Timestamps


class Category(Timestamps):
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
        upload_to="mediafiles/category_pictures",
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name


class ProductPictures(models.Model):
    picture = models.ImageField(
        upload_to="mediafiles/product_pictures",
        null=False,
        blank=False,
    )


class Product(Timestamps):
    NAME_MAX_LENGTH = 50
    NAME_MIN_LENGTH = 3

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(
                limit_value=NAME_MIN_LENGTH,
                message=f"{__name__} name must contain at latest {NAME_MIN_LENGTH}",
            ),
        ),
        error_messages={
            "max_length": f"{__name__} name must conatain max {NAME_MAX_LENGTH}",
        }
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    count = models.SmallIntegerField(
        null=False,
        blank=False,
        default=0,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    pictures = models.ManyToManyField(
        ProductPictures,
        related_name="products",
    )
