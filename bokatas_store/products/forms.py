from django import forms

from bokatas_store.products.models import Product, Category


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.ImageField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class BaseProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "price", "description", "count", "category")


class CreateProductForm(BaseProductForm):
    images = MultipleFileField()


class BaseCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name", "picture")


class CreateCategoryForm(BaseCategoryForm):
    ...