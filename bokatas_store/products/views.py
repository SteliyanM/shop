from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic as views

from bokatas_store.products.forms import CreateProductForm
from bokatas_store.products.models import ProductPicture


class CreateProductView(views.CreateView):
    form_class = CreateProductForm
    template_name = "products/create.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        if form.is_valid():
            product = form.save()

            images = form.cleaned_data["images"]

            ProductPicture.objects.bulk_create([
                ProductPicture(product=product, picture=image) for image in images
            ])

        return HttpResponseRedirect(self.success_url)
