from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from bokatas_store import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("bokatas_store.web.urls")),
    path("accounts/", include("bokatas_store.accounts.urls")),
    path("profiles/", include("bokatas_store.profiles.urls")),
    path("products/", include("bokatas_store.products.urls")),
    path("category/", include("bokatas_store.categories.urls")),
    path("shopping-cart/", include("bokatas_store.shopping_cart.urls")),
    path("order/", include("bokatas_store.orders.urls")),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
