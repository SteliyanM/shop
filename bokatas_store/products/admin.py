from django.contrib import admin

from bokatas_store.products.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "picture")
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description", "count", "category")
    list_filters = ("name", "price", "description", "count", "category")
    search_fields = ("name", "price", "description", "count", "category")

