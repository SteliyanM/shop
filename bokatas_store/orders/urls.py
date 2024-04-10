from django.urls import path, include
from .views import CreateOrderView, AddressOrderView, PaymentOrderView, ListOrdersView, DetailsOrderView


urlpatterns = (
    path("create/", CreateOrderView.as_view(), name="create-order"),
    path("address/", AddressOrderView.as_view(), name="create-address-to-order"),
    path("list/", ListOrdersView.as_view(), name="list-orders"),
    path("<int:pk>/", include([
        path("", DetailsOrderView.as_view(), name="details-order"),
        path("payment/",  PaymentOrderView.as_view(), name="create-payment-to-order"),
    ])),
)
