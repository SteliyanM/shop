from django.urls import path
from .views import UserLoginView, UserRegisterView, logout_view


urlpatterns = (
    path("signin/", UserLoginView.as_view(), name="login-user"),
    path("register/", UserRegisterView.as_view(), name="register-user"),
    path("logout/", logout_view, name="logout-user"),
)
