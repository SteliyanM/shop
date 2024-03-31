from django.contrib import admin

from .models import UserProfile, UserPayment, UserAddress


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "gender", "get_email")
    search_fields = ("first_name", "last_name", "gender",)
    list_filter = ("first_name", "last_name", "gender",)

    @admin.display(empty_value="no email")
    def get_email(self, obj: UserProfile):
        return obj.user.email


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ("address1", "address2", "zip_code", "city", "country",)
    search_fields = ("address1", "address2", "zip_code", "city", "country",)
    list_filter = ("zip_code", "city", "country",)


@admin.register(UserPayment)
class UserPaymentAdmin(admin.ModelAdmin):
    list_display = ("payment_method", "is_successful",)
    search_fields = ("user", "payment_method", "is_successful",)
