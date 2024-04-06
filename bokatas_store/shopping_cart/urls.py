from django.urls import path, include
from .views import DetailsShoppingCartView, add_product_to_shoppingcart_and_order, remove_product_to_shoppingcart_and_order


urlpatterns = (
    path("", DetailsShoppingCartView.as_view(), name="details-shopping-cart"),
    path("<int:pk>/", include([
        path("add/", add_product_to_shoppingcart_and_order, name="add-product-to-shopping-cart"),
        path("remove/", remove_product_to_shoppingcart_and_order, name="remove-product-to-shopping-cart"),
    ])),
)
