from django import forms

from bokatas_store.profiles.models import UserAddress, UserPayment


class ProductQuantityForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label="Quantity", initial=1)

    def __init__(self, *args, **kwargs):
        self.product = kwargs.pop('product', None)
        super(ProductQuantityForm, self).__init__(*args, **kwargs)

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is None:
            raise forms.ValidationError("Please enter a valid quantity.")
        if quantity > self.product.count:
            raise forms.ValidationError(f"The selected quantity exceeds the available stock count."
                                        f" Product current count is {self.product.count}")
        return quantity


class AddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ("address1", "address2", "zip_code", "city", "country")

        labels = {
            "address1": "First address",
            "address2": "Second address",
        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = UserPayment
        fields = ("payment_method",)
