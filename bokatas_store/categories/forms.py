from bokatas_store.categories.models import Category
from django import forms


class BaseCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name", "picture")


class CreateCategoryForm(BaseCategoryForm):
    ...
