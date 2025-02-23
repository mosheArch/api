from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class PredictionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "predictions"
    verbose_name = _("Predictions")

