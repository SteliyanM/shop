from django.urls import path

from bokatas_store.web.views import IndexView

urlpatterns = (
    path("", IndexView.as_view(), name="index"),
)
