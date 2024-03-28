from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import UserProfile, UserAddress, UserPayment

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "phone_number",)
    search_fields = ("email", "phone_number",)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "gender")
    search_fields = ("first_name", "last_name", "gender")
    list_filter = ("first_name", "last_name", "gender")


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ("address1", "address2", "zip_code", "city", "country",)
    search_fields = ("address1", "address2", "zip_code", "city", "country",)
    list_filter = ("zip_code", "city", "country",)


@admin.register(UserPayment)
class UserPaymentAdmin(admin.ModelAdmin):
    list_display = ("payment_method", "is_successful",)
    search_fields = ("user", "payment_method", "is_successful",)

