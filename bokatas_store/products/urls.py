from django.urls import path, include
from .views import CreateProductView


urlpatterns = (
    path("create/", CreateProductView.as_view(), name="create-product"),
)
