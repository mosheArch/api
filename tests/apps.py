from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class TestsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tests"
    verbose_name = _("Tests")
