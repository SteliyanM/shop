from django import forms
from phonenumber_field.formfields import PhoneNumberField

from bokatas_store.profiles.models import UserProfile


class BaseUserForm(forms.ModelForm):
    email = forms.EmailField()
    phone_number = PhoneNumberField(region="BG")

    class Meta:
        model = UserProfile
        fields = ("email", "phone_number", "first_name", "last_name", "gender", "profile_picture")


class EditUserForm(BaseUserForm):
    ...


class DeleteUserForm(BaseUserForm):
    email = forms.EmailField(disabled=True)
    phone_number = PhoneNumberField(region="BG", disabled=True)

    class Meta:
        model = UserProfile
        fields = ("email", "phone_number", "first_name", "last_name", "gender")

    def __init__(self, *args, **kwargs):
        super(BaseUserForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['disabled'] = True






