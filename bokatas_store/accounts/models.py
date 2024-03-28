from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator

from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from bokatas_store.accounts.managers import BokataStoreUserManager
from bokatas_store.orders.models import Order
# from bokatas_store.accounts import mixins
from core.model_mixins import Timestamps


class BokataStoreUser(Timestamps, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    phone_number = PhoneNumberField(
        region="BG",
        unique=True,
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = BokataStoreUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number"]


class UserField(models.Model):
    class Meta:
        abstract = True

    user = models.OneToOneField(
        BokataStoreUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class UserProfile(UserField):
    class GenderChoices(models.TextChoices):
        MALE = "m"
        FEMALE = "f"
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
        upload_to="mediafiles/profile_pictures",
        null=True,
        blank=True,
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


class UserPayment(UserField):
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
    )

