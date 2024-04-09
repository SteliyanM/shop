from django.urls import path, include
from .views import CreateOrderView, AddressOrderView, PaymentOrderView, ListOrdersView


urlpatterns = (
    path("create/", CreateOrderView.as_view(), name="create-order"),
    path("address/", AddressOrderView.as_view(), name="create-address-to-order"),
    path("list/", ListOrdersView.as_view(), name="list-orders"),
    path("<int:pk>/", include([
        path("payment/",  PaymentOrderView.as_view(), name="create-payment-to-order"),
    ])),
)
