from django.shortcuts import render, redirect
from django.views import generic as views

from .forms import ProductQuantityForm
from .models import ProductQuantity, Order


class CreateOrderView(views.TemplateView):
    template_name = "orders/create.html"

    def _get_shopping_cart_products(self):
        return self.request.user.shoppingcart.products.all()

    def _calculate_order_total_price(self, order_id):
        products_count = ProductQuantity.objects.filter(order_id=order_id).select_related("product")
        total_sum = 0

        for product_count in products_count:
            total_sum += product_count.product.price * product_count.quantity

        return total_sum

    def get(self, request, *args, **kwargs):
        products = self._get_shopping_cart_products()
        forms = {product: ProductQuantityForm(prefix=product.id) for product in products}

        return render(request, self.get_template_names(), {'products_and_forms': forms})

    def post(self, request, *args, **kwargs):
        products = self._get_shopping_cart_products()
        order = Order.objects.create(total_price=32, status=False, user=self.request.user)
        forms = {}

        form_errors = False

        for product in products:
            form = ProductQuantityForm(request.POST, prefix=product.id, product=product)
            forms[product] = form
            if form.is_valid():
                quantity = form.cleaned_data['quantity']
                ProductQuantity.objects.create(product=product, quantity=quantity, order=order)
            else:
                form_errors = True

        if form_errors:
            order.delete()
            return render(request, self.get_template_names(), {'products_and_forms': forms})

        order.total_price = self._calculate_order_total_price(order.pk)
        order.save()

        return redirect("index")


