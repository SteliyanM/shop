from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from bokatas_store.accounts.managers import BokataStoreUserManager
from bokatas_store.core.model_mixins import Timestamps


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
