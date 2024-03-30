from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import BaseUserCreationForm
from django.core.exceptions import ValidationError

from phonenumber_field.formfields import PhoneNumberField

from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class UserLoginForm(forms.Form):
    email = forms.CharField(
        label=_("Email",)
    )

    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

    error_messages = {
        "invalid_login": _(
            "Incorrect email and password. Note that both fields may be case-sensitive."
        ),
        "inactive": _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email is not None and password:
            self.user_cache = authenticate(
                self.request, username=email, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error(email)
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(
                self.error_messages["inactive"],
                code="inactive",
            )

    def get_user(self):
        return self.user_cache

    def get_invalid_login_error(self, email):
        return ValidationError(
            self.error_messages["invalid_login"],
            code="invalid_login",
            params={"email": email},
        )


class UserRegisterForm(BaseUserCreationForm):
    class Meta:
        model = UserModel
        fields = ("email", "phone_number",)
        field_classes = {"email": forms.EmailField, "phone_number": PhoneNumberField}


