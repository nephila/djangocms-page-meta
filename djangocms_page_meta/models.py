import ast

from cms.extensions import PageExtension, TitleExtension
from cms.extensions.extension_pool import extension_pool
from cms.models import Page, Title
from django.conf import settings
from django.core.cache import cache
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from filer.fields.file import FilerFileField
from meta import settings as meta_settings

from .utils import get_cache_key, get_metatags

try:
    from aldryn_snake.template_api import registry
except ImportError:
    registry = None


class PageMeta(PageExtension):
    image = FilerFileField(
        null=True,
        blank=True,
        related_name="djangocms_page_meta_page",
        help_text=_("Used if title image is empty."),
        on_delete=models.CASCADE,
    )
    og_type = models.CharField(
        _("Resource type"),
        max_length=255,
        choices=meta_settings.FB_TYPES,
        blank=True,
        help_text=_("Use Article for generic pages."),
    )
    og_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Author account"),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    og_author_url = models.CharField(_("Author Facebook URL"), max_length=255, default="", blank=True)
    og_author_fbid = models.CharField(
        _("Author Facebook ID"), max_length=16, default="", blank=True, help_text=_("Use Facebook numeric ID.")
    )
    og_publisher = models.CharField(_("Website Facebook URL"), max_length=255, default="", blank=True)
    og_app_id = models.CharField(_("Facebook App ID"), max_length=255, default="", blank=True)
    fb_pages = models.CharField(_("Facebook Pages ID"), max_length=255, default="", blank=True)
    twitter_author = models.CharField(
        _("Author Twitter Account"), max_length=255, default="", blank=True, help_text=_("'@' character not required.")
    )
    twitter_site = models.CharField(
        _("Website Twitter Account"),
        max_length=255,
        default="",
        blank=True,
        help_text=_("'@' character not required."),
    )
    twitter_type = models.CharField(
        _("Resource type"), max_length=255, choices=meta_settings.TWITTER_TYPES, blank=True
    )
    schemaorg_type = models.CharField(
        _("Resource type"),
        max_length=255,
        choices=meta_settings.SCHEMAORG_TYPES,
        blank=True,
        help_text=_("Use Article for generic pages."),
    )
    robots = models.CharField(_("Robots meta tag"), max_length=512, blank=True)

    class Meta:
        verbose_name = _("Page meta info (all languages)")
        verbose_name_plural = _("Page meta info (all languages)")

    def __str__(self):
        return _("Page Meta for {0}").format(self.extended_object)

    def copy_relations(self, oldinstance, language):
        # Remove old refs to prep for copying
        self.extra.all().delete()

        # Copy everyting to published page instance
        for item in oldinstance.extra.all():
            item.pk = None
            item.page = self
            item.save()

    @property
    def robots_list(self):
        if self.robots:
            return ast.literal_eval(self.robots)
        return None


extension_pool.register(PageMeta)


class TitleMeta(TitleExtension):
    image = FilerFileField(
        null=True,
        blank=True,
        related_name="djangocms_page_meta_title",
        help_text=_("If empty, page image will be used for all languages."),
        on_delete=models.CASCADE,
    )
    keywords = models.CharField(max_length=2000, default="", blank=True)
    description = models.CharField(max_length=2000, default="", blank=True)
    og_description = models.CharField(_("Facebook Description"), max_length=2000, default="", blank=True)
    twitter_description = models.CharField(_("Twitter Description"), max_length=2000, default="", blank=True)
    schemaorg_name = models.CharField(
        _("Schemaorg Name"), max_length=255, blank=True, help_text=_("Name of the item.")
    )
    schemaorg_description = models.CharField(
        _("Schemaorg Description"), max_length=255, blank=True, help_text=_("Description of the item.")
    )

    class Meta:
        verbose_name = _("Page meta info (language-dependent)")
        verbose_name_plural = _("Page meta info (language-dependent)")

    def __str__(self):
        return _("Title Meta for {0}").format(self.extended_object)

    @property
    def locale(self):
        if self.extended_object.language.find("_") > -1:
            return self.extended_object.language
        else:
            return None

    def copy_relations(self, oldinstance, language):
        # Remove old refs to prep for copying
        self.extra.all().delete()

        # Copy everyting to published page instance
        for item in oldinstance.extra.all():
            item.pk = None
            item.title = self
            item.save()


extension_pool.register(TitleMeta)


class GenericMetaAttribute(models.Model):
    DEFAULT_ATTRIBUTE = "name"
    page = models.ForeignKey(PageMeta, null=True, blank=True, related_name="extra", on_delete=models.CASCADE)
    title = models.ForeignKey(TitleMeta, null=True, blank=True, related_name="extra", on_delete=models.CASCADE)
    attribute = models.CharField(
        _("attribute"),
        max_length=200,
        help_text=_("Custom attribute"),
        default="",
        blank=True,
    )
    name = models.CharField(
        _("name"),
        max_length=200,
        help_text=_("Meta attribute name"),
    )
    value = models.CharField(
        _("value"),
        max_length=2000,
        help_text=_("Meta attribute value"),
    )

    class Meta:
        verbose_name = _("Page meta info (language-dependent)")
        verbose_name_plural = _("Page meta info (language-dependent)")

    def __str__(self):
        if self.page:
            return _("Attribute {0} for {1}").format(self.name, self.page)
        if self.title:
            return _("Attribute {0} for {1}").format(self.name, self.title)


class DefaultMetaImage(models.Model):
    image = FilerFileField(
        null=True,
        blank=True,
        related_name="djangocms_page_meta_default_image",
        help_text=_(
            "Default image for og:image, twitter:image and schema.org image.\n"
            "You can override this by setting the image in Meta-information page extension."
        ),
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = _("Default meta image")
        verbose_name_plural = _("Default meta images")

    def __str__(self):
        return self.image.label if self.image else str(self.pk)


# Cache cleanup when deleting pages / editing page extensions
@receiver(pre_delete, sender=Page)
def cleanup_page(sender, instance, **kwargs):
    for language in instance.get_languages():
        key = get_cache_key(instance, language)
        cache.delete(key)


@receiver(pre_delete, sender=Title)
def cleanup_title(sender, instance, **kwargs):
    key = get_cache_key(instance.page, instance.language)
    cache.delete(key)


@receiver(post_save, sender=PageMeta)
@receiver(pre_delete, sender=PageMeta)
def cleanup_pagemeta(sender, instance, **kwargs):
    for language in instance.extended_object.get_languages():
        key = get_cache_key(instance.extended_object, language)
        cache.delete(key)


@receiver(post_save, sender=TitleMeta)
@receiver(pre_delete, sender=TitleMeta)
def cleanup_titlemeta(sender, instance, **kwargs):
    key = get_cache_key(instance.extended_object.page, instance.extended_object.language)
    cache.delete(key)


if registry:
    registry.add_to_head(get_metatags)
