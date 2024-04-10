from django.core.validators import RegexValidator
from django.db import models
from django_countries.fields import CountryField

from bokatas_store.accounts.mixins import UserField
from bokatas_store.orders.models import Order


class UserProfile(UserField):
    class GenderChoices(models.TextChoices):
        MALE = "male"
        FEMALE = "female"
        OTHER = "other"
        PREFER_NOT_TO_SAY = "prefer not to say"

    FIRST_NAME_MAX_LENGTH = 50

    LAST_NAME_MAX_LENGTH = 50

    GENDER_MAX_LENGTH = 20

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        blank=True,
        null=True,
        validators=(
            RegexValidator(
                regex=r"^[a-zA-Z]+$",
                message="First name can contain only letters",
            ),
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        blank=True,
        null=True,
        validators=(
            RegexValidator(
                regex=r"^[a-zA-Z]+$",
                message="Last name can contain only letters",
            ),
        )
    )

    gender = models.CharField(
        max_length=20,
        choices=GenderChoices,
        null=True,
        blank=True,
    )

    profile_picture = models.ImageField(
        upload_to="profile_pictures",
        default="profile_pictures/default_profile_picture.webp"
    )


class UserAddress(UserField):
    address1 = models.CharField(
        "Address line 1",
        max_length=1024,
    )

    address2 = models.CharField(
        "Address line 2",
        max_length=1024,
    )

    zip_code = models.CharField(
        "ZIP / Postal code",
        max_length=12,
    )

    city = models.CharField(
        "City",
        max_length=1024,
    )

    country = CountryField()


class UserPayment(models.Model):
    class PaymentMethod(models.TextChoices):
        CREDIT_CARD = 'credit card'
        PAYPAL = 'paypal'
        BANK_TRANSFER = 'bank transfer'
        CASH = 'cash'

    payment_method = models.CharField(
        max_length=20,
        choices=PaymentMethod.choices,
        default=PaymentMethod.CREDIT_CARD
    )

    is_successful = models.BooleanField(
        default=False
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        primary_key=True
    )
