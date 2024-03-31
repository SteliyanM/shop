from django.views import generic as views

from bokatas_store.products.models import Category


class IndexView(views.ListView):
    queryset = Category
    template_name = "web/index.html"
