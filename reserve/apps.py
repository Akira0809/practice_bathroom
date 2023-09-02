from django.apps import AppConfig


class ReserveConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reserve'

    def ready(self):
        from .ap_scheduler import start
        start()
