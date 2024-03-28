from django.db import models

from bokatas_store.accounts.models import UserField
from bokatas_store.products.models import Product


class Order(UserField):
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

    products = models.ManyToManyField(
        Product,
        related_name="orders",
    )
