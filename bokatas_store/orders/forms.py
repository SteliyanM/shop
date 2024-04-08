from django import forms


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
