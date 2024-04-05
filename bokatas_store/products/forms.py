from django import forms

from bokatas_store.products.models import Product, Review


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


class BaseReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("rating", "description")


class CreateReviewForm(BaseReviewForm):
    rating = forms.IntegerField(
        max_value=5,
        min_value=1,
        required=True,
    )

    class Meta:
        model = Review
        fields = ("rating", "description",)


class AddProductToCartBaseForm(forms.Form):
    product_id = forms.IntegerField(required=False)
