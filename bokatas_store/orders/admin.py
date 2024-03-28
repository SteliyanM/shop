from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("total_price", "status")
    search_fields = ("total_price", "status")
    list_filter = ("total_price", "status",)

