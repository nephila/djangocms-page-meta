from cms.admin.pageadmin import PageAdmin
from cms.extensions import PageExtensionAdmin, TitleExtensionAdmin
from cms.utils import get_language_from_request
from django.conf import settings
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .forms import GenericAttributeInlineForm, PageMetaAdminForm, TitleMetaAdminForm
from .models import DefaultMetaImage, GenericMetaAttribute, PageMeta, TitleMeta


@admin.register(DefaultMetaImage)
class DefaultMetaImageAdmin(admin.ModelAdmin):
    actions = None

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class GenericAttributePageInline(admin.TabularInline):
    model = GenericMetaAttribute
    form = GenericAttributeInlineForm
    fields = ("page", "attribute", "name", "value")
    extra = 1


class GenericAttributeTitleInline(admin.TabularInline):
    model = GenericMetaAttribute
    form = GenericAttributeInlineForm
    fields = ("title", "attribute", "name", "value")
    extra = 1


@admin.register(PageMeta)
class PageMetaAdmin(PageExtensionAdmin):
    raw_id_fields = ("og_author",)
    form = PageMetaAdminForm
    inlines = (GenericAttributePageInline,)
    fieldsets = (
        (None, {"fields": ("image",)}),
        (
            _("OpenGraph"),
            {
                "fields": (
                    "og_type",
                    ("og_author", "og_author_url", "og_author_fbid"),
                    ("og_publisher", "og_app_id", "fb_pages"),
                ),
                "classes": ("collapse",),
            },
        ),
        (_("Twitter Cards"), {"fields": ("twitter_type", "twitter_author"), "classes": ("collapse",)}),
        (_("Schema.org microdata"), {"fields": ("schemaorg_type",), "classes": ("collapse")}),
        (_("Robots"), {"fields": ("robots",), "classes": ("collapse")}),
    )

    class Media:
        css = {"all": ("{}djangocms_page_meta/css/{}".format(settings.STATIC_URL, "djangocms_page_meta_admin.css"),)}

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


@admin.register(TitleMeta)
class TitleMetaAdmin(TitleExtensionAdmin):
    form = TitleMetaAdminForm
    inlines = (GenericAttributeTitleInline,)

    class Media:
        css = {"all": ("{}djangocms_page_meta/css/{}".format(settings.STATIC_URL, "djangocms_page_meta_admin.css"),)}

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


# Monkey patch the PageAdmin with a new get_form method
_BASE_PAGEADMIN__GET_FORM = PageAdmin.get_form


def get_form(self, request, obj=None, **kwargs):
    """
    Patched method for PageAdmin.get_form.

    Returns a page form without the base field 'meta_description' which is
    overridden in djangocms-page-meta.

    This is triggered in the page add view and in the change view if
    the meta description of the page is empty.
    """
    language = get_language_from_request(request, obj)
    form = _BASE_PAGEADMIN__GET_FORM(self, request, obj, **kwargs)
    if not obj or not obj.get_meta_description(language=language):
        form.base_fields.pop("meta_description", None)

    return form


PageAdmin.get_form = get_form
