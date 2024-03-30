from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from bokatas_store import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("bokatas_store.web.urls")),
    path('accounts/', include("bokatas_store.accounts.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
