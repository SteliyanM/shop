from django.contrib import admin

from bokatas_store.products.models import Product, ProductPicture


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description", "count", "category")
    list_filters = ("name", "price", "description", "count", "category")
    search_fields = ("name", "price", "description", "count", "category")


@admin.register(ProductPicture)
class ProductPicturesAdmin(admin.ModelAdmin):
    list_display = ("picture", "product_name")

    @admin.display(empty_value="no product")
    def product_name(self, obj: ProductPicture):
        return obj.products.first().name
