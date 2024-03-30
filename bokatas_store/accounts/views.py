from django.contrib.auth import views as auth_views, logout, login
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views import generic as views

from bokatas_store.accounts.forms import UserLoginForm, UserRegisterForm


class UserLoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = UserLoginForm
    redirect_authenticated_user = reverse_lazy("index")


class UserRegisterView(views.CreateView):
    form_class = UserRegisterForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)
        return response


def logout_view(request):
    logout(request)

    return redirect("index")

