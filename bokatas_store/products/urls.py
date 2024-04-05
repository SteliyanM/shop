from django.urls import path, include
from .views import CreateProductView, DetailsProductView


urlpatterns = (
    path("create/", CreateProductView.as_view(), name="create-product"),
    path("<slug:slug>", include([
        path("", DetailsProductView.as_view(), name="details-product"),
    ])),
)
