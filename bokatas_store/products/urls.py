from django.urls import path, include
from .views import CreateProductView, CreateCategoryView


urlpatterns = (
    path("create/", CreateProductView.as_view(), name="create-product"),
    path("category/", include([
        path("create/", CreateCategoryView.as_view(), name="create-category"),
    ])),
)
