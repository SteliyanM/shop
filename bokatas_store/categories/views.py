from django.db.models import Count, Q, Min, Max
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views
from .forms import CreateCategoryForm

from .models import Category
from ..core.view_mixins import AdminRequired
from ..products.models import Product


class CreateCategoryView(AdminRequired, views.CreateView):
    form_class = CreateCategoryForm
    template_name = "categories/create.html"
    success_url = reverse_lazy("list-category")


class ListCategoryView(views.ListView):
    template_name = "categories/list.html"
    queryset = (Category.objects.prefetch_related("product_set")
                .annotate(product_count=Count("product"))
                .order_by("-product_count"))


class DetailsCategoryView(views.ListView):
    template_name = "categories/details.html"

    def get_queryset(self):
        return (Product.objects
                    .prefetch_related("productpicture_set")
                    .prefetch_related("category")
                    .filter(category__slug=self.kwargs["slug"]))

    def post(self):
        ...

    @property
    def _get_min_max_price(self):
        if Product.objects.exists():
            price_range = Product.objects.filter(category__slug=self.kwargs["slug"]).aggregate(
                min_price=Min('price'),
                max_price=Max('price')
            )

            return price_range["min_price"], price_range["max_price"]

        else:
            return 0, 0

    @property
    def get_search(self):
        return self.request.GET.get("search", None)

    @property
    def get_price_range(self):
        return self.request.GET.get("price_range", None)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        products = self.get_queryset()

        search = self.get_search
        price_range = self.get_price_range

        if price_range:
            min_price, max_price = [int(x) for x in price_range.split("-")]

            context["min_price_value"], context["max_price_value"] = min_price, max_price

            products = products.filter(price__range=[min_price, max_price])

        else:
            min_price, max_price = self._get_min_max_price
            context["min_price_value"], context["max_price_value"] = min_price, max_price
            context["min_price"], context["max_price"] = min_price, max_price

        if search:
            query = Q(name__icontains=search) | Q(description__icontains=search)

            products = products.filter(query)

        context["products"] = products
        context["search"] = search

        category = get_object_or_404(Category, slug=self.kwargs["slug"])
        context["category"] = category

        min_price, max_price = self._get_min_max_price

        context["min_price"], context["max_price"] = int(min_price), int(max_price)

        return context
