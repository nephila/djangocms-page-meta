from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PageMetaConfig(AppConfig):
    name = "djangocms_page_meta"
    verbose_name = _("django CMS Page Meta")
