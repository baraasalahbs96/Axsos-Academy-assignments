from django.apps import AppConfig


class ArbitrationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "arbitration"
    verbose_name = "التحكيم الشرعي"

    def ready(self):
        from . import signals  # noqa: F401
