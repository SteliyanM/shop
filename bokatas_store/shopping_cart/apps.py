from django.apps import AppConfig


class ShoppingCartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bokatas_store.shopping_cart'

    def ready(self):
        import bokatas_store.shopping_cart.signals
