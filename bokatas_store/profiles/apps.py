from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bokatas_store.profiles'

    def ready(self):
        import bokatas_store.profiles.signals
