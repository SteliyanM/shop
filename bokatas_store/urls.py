from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from bokatas_store import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("bokatas_store.web.urls")),
    path('accounts/', include("bokatas_store.accounts.urls")),
    path('profiles/', include("bokatas_store.profiles.urls")),
    path('products/', include("bokatas_store.products.urls")),
    path('category/', include("bokatas_store.categories.urls")),
    path('shopping-cart/', include("bokatas_store.shopping_cart.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
