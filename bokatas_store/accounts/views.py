from django.contrib.auth import views as auth_views, logout, login
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse

from django.views import generic as views

from bokatas_store.accounts.forms import UserLoginForm, UserRegisterForm


class UserLoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = UserLoginForm
    redirect_authenticated_user = reverse_lazy("index")

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']

        if remember_me:
            self.request.session.set_expiry(604800)
        else:
            self.request.session.set_expiry(0)

        return super().form_valid(form)


class UserRegisterView(views.CreateView):
    form_class = UserRegisterForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)
        return response


class UserChangePasswordView(auth_views.PasswordChangeView):
    template_name = "accounts/change_password.html"

    def get_success_url(self):
        return reverse("details-profile", kwargs={"pk": self.request.user.pk})


def logout_view(request):
    logout(request)

    return redirect("index")

