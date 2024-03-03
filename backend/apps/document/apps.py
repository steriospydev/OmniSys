from django.apps import AppConfig


class DocumentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.document'

    def ready(self):
       from .models import update_order_totals