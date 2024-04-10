from django.db.models import Avg
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from bokatas_store.core.view_mixins import AdminRequired
from bokatas_store.products.forms import CreateProductForm, CreateReviewForm
from bokatas_store.products.models import ProductPicture, Product, Review


class CreateProductView(AdminRequired, views.CreateView):
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


class DetailsProductView(views.DetailView):
    queryset = (Product.objects
                .prefetch_related("productpicture_set")
                .prefetch_related("review_set")
                .prefetch_related("category")
                .prefetch_related("review_set__user")
                )
    template_name = "products/details.html"

    def post(self, request, *args, **kwargs):
        form = CreateReviewForm(request.POST)

        if form.is_valid():
            form.instance.user = self.request.user
            form.instance.product = Product.objects.get(slug=kwargs["slug"])
            form.save()

            return HttpResponseRedirect(reverse("details-product", kwargs=kwargs))

        return render(request, self.template_name, {"form": form, "object": self.get_object()})

    def get_context_data(self, **kwargs):
        form = CreateReviewForm()
        context = super().get_context_data(**kwargs)
        context["form"] = form

        avg_rating = Review.objects.filter(product=self.object).aggregate(Avg("rating")).get("rating__avg", None)
        context["avg_rating"] = avg_rating

        return context
