from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from bokatas_store.categories.models import Category
from bokatas_store.core.model_mixins import Timestamps, SlugFieldMixin

UserModel = get_user_model()


class Product(SlugFieldMixin, Timestamps):
    NAME_MAX_LENGTH = 50
    NAME_MIN_LENGTH = 3

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        null=False,
        blank=False,
        unique=True,
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


class ProductPicture(models.Model):
    class Meta:
        verbose_name_plural = "product pictures"

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    picture = models.ImageField(
        upload_to="product_pictures",
        null=False,
        blank=False,
    )


class Review(Timestamps):
    rating = models.DecimalField(
        null=False,
        blank=False,
        max_digits=3,
        decimal_places=1,
        validators=(
            MinValueValidator(0.5),
            MaxValueValidator(5),
        )
    )

    description = models.TextField()

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
