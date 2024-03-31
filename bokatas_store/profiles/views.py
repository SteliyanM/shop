from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views import generic as views

from bokatas_store.profiles.models import UserProfile

UserModel = get_user_model()


class DetailsProfileView(views.DetailView):
    queryset = UserProfile.objects.prefetch_related("user").all()
    template_name = "profiles/details.html"

    def get_object(self, queryset=None):
        try:
            super().get_object(queryset)
        except:
            UserProfile.objects.create(user=UserModel.objects.get(pk=self.request.user.pk))

        return super().get_object(queryset)


class EditProfileView(views.UpdateView):
    queryset = UserProfile.objects.all()
    template_name = "profiles/edit.html"
    fields = ("first_name", "last_name", "gender", "profile_picture")

    def get_success_url(self):
        return reverse("details-profile", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        cleaned_pf = form.cleaned_data.get("profile_picture")

        if not cleaned_pf:
            form.cleaned_data["profile_picture"] = "profile_pictures/default_profile_picture.webp"

        return super().form_valid(form)

    def get_object(self, queryset=None):
        try:
            super().get_object(queryset)
        except:
            UserProfile.objects.create(user=UserModel.objects.get(pk=self.request.user.pk))

        return super().get_object(queryset)