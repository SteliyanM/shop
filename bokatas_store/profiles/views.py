from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from bokatas_store.profiles.forms import EditUserForm, DeleteUserForm
from bokatas_store.profiles.models import UserProfile

from django import forms

UserModel = get_user_model()


class DetailsProfileView(auth_mixins.LoginRequiredMixin, views.DetailView):
    queryset = UserProfile.objects.prefetch_related("user").all()
    template_name = "profiles/details.html"

    def get_object(self, queryset=None):
        try:
            super().get_object(queryset)
        except:
            UserProfile.objects.create(user=UserModel.objects.get(pk=self.request.user.pk))

        return super().get_object(queryset)


class EditProfileView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    queryset = UserProfile.objects.all()
    template_name = "profiles/edit.html"
    form_class = EditUserForm

    def get_success_url(self):
        return reverse("details-profile", kwargs={"pk": self.object.pk})

    def get_object(self, queryset=None):
        try:
            super().get_object(queryset)
        except:
            UserProfile.objects.create(user=UserModel.objects.get(pk=self.request.user.pk))

        return super().get_object(queryset)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        form.fields["email"].initial = self.request.user.email
        form.fields["phone_number"].initial = self.request.user.phone_number

        return form

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        phone_number = form.cleaned_data["phone_number"]

        if UserModel.objects.exclude(pk=self.request.user.pk).filter(email=email).exists():
            form.add_error('email', forms.ValidationError("User with that email already exists", code="invalid"))
        else:
            self.request.user.email = email

        if UserModel.objects.exclude(pk=self.request.user.pk).filter(phone_number=phone_number).exists():
            form.add_error('phone_number', forms.ValidationError("User with that phone number already exists", code="invalid"))
        else:
            self.request.user.phone_number = phone_number

        self.request.user.save()

        if form.is_valid():
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class DeleteProfileView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    template_name = "profiles/delete.html"
    queryset = UserModel.objects.prefetch_related("userprofile").all()
    success_url = reverse_lazy("index")
    form_class = DeleteUserForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # form.instance = self.object
        form.fields['email'].initial = self.object.email
        form.fields['first_name'].initial = self.object.userprofile.first_name
        form.fields['last_name'].initial = self.object.userprofile.last_name
        form.fields['gender'].initial = self.object.userprofile.gender
        form.fields['phone_number'].initial = self.object.phone_number

        return form
