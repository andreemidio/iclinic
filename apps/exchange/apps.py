from django.apps import AppConfig


class ExchangeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.exchange'

    def ready(self):
        try:
            import apps.exchange.tasks
        except ImportError:
            pass
        