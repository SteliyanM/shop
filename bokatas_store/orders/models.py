from django.contrib.auth import get_user_model
from django.db import models

from bokatas_store.accounts.mixins import UserField
from bokatas_store.products.models import Product


UserModel = get_user_model()


class Order(models.Model):
    total_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=False,
        blank=False,
    )

    status = models.BooleanField(
        null=False,
        blank=False,
        default=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class ProductQuantity(models.Model):
    quantity = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )
