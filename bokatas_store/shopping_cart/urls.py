from django.urls import path
from .views import DetailsShoppingCartView, add_product_to_shoppingcart


urlpatterns = (
    path("", DetailsShoppingCartView.as_view(), name="details-shopping-cart"),
    path("add/<int:pk>/", add_product_to_shoppingcart, name="add-product-to-shopping-cart"),
)
