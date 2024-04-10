from django.contrib.auth import get_user_model
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import generic as views

from bokatas_store.products.models import Product
from bokatas_store.shopping_cart.models import ShoppingCart


UserModel = get_user_model()


class DetailsShoppingCartView(auth_mixins.LoginRequiredMixin, views.TemplateView):
    template_name = "shopping_cart/details.html"
    login_url = reverse_lazy("login-user")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        shopping_cart = ShoppingCart.objects.get(user_id=self.request.user.pk)
        context["products"] = shopping_cart.products.all()

        return context


@login_required(login_url=reverse_lazy("login-user"))
def add_product_to_shoppingcart_and_order(request, pk):
    product = Product.objects.get(pk=pk)
    request.user.shoppingcart.products.add(product)

    return redirect(reverse('details-product', kwargs={"slug": product.slug}))


@login_required(login_url=reverse_lazy("login-user"))
def remove_product_to_shoppingcart_and_order(request, pk):
    product = Product.objects.get(pk=pk)

    if product and product in request.user.shoppingcart.products.all():
        request.user.shoppingcart.products.remove(product)

    return redirect(reverse('details-shopping-cart'))

