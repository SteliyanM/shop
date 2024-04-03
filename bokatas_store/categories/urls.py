from django.urls import path, include
from .views import CreateCategoryView, ListCategoryView, DetailsCategoryView


urlpatterns = (
    path("create/", CreateCategoryView.as_view(), name="create-category"),
    path("list/", ListCategoryView.as_view(), name="list-category"),
    path("<slug:slug>/", include([
        path("", DetailsCategoryView.as_view(), name="details-category"),
    ])),
)
