from django.contrib.auth import get_user_model
from django.db import models

from bokatas_store.products.models import Product


UserModel = get_user_model()


class ShoppingCart(models.Model):
    products = models.ManyToManyField(
        Product,
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
