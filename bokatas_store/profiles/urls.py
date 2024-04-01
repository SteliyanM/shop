from django.urls import path, include
from .views import DetailsProfileView, EditProfileView, DeleteProfileView

urlpatterns = (
    path("<int:pk>/", include([
        path("", DetailsProfileView.as_view(), name="details-profile"),
        path("edit/", EditProfileView.as_view(), name="edit-profile"),
        path("delete/", DeleteProfileView.as_view(), name="delete-profile"),
    ])),
)
