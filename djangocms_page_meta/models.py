# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.extensions import PageExtension, TitleExtension
from cms.extensions.extension_pool import extension_pool
from cms.models import Page, Title
from django.conf import settings
from django.core.cache import cache
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from filer.fields.file import FilerFileField
from meta import settings as meta_settings

from .utils import get_metatags  # noqa
from .utils import get_cache_key

try:
    from aldryn_snake.template_api import registry
except:
    registry = None


@python_2_unicode_compatible
class PageMeta(PageExtension):
    image = FilerFileField(
        null=True, blank=True, related_name='djangocms_page_meta_page',
        help_text=_('Used if title image is empty.')
    )
    og_type = models.CharField(
        _('Resource type'), max_length=255, choices=meta_settings.FB_TYPES, blank=True,
        help_text=_('Use Article for generic pages.')
    )
    og_author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_('Author account'), null=True, blank=True
    )
    og_author_url = models.CharField(
        _('Author Facebook URL'), max_length=255, default='', blank=True
    )
    og_author_fbid = models.CharField(
        _('Author Facebook ID'), max_length=16, default='', blank=True,
        help_text=_('Use Facebook numeric ID.')
    )
    og_publisher = models.CharField(
        _('Website Facebook URL'), max_length=255, default='', blank=True
    )
    og_app_id = models.CharField(
        _('Facebook App ID'), max_length=255, default='', blank=True
    )
    fb_pages = models.CharField(
        _('Facebook Pages ID'), max_length=255, default='', blank=True
    )
    twitter_author = models.CharField(
        _('Author Twitter Account'), max_length=255, default='', blank=True,
        help_text=_('\'@\' character not required.')
    )
    twitter_site = models.CharField(
        _('Website Twitter Account'), max_length=255, default='', blank=True,
        help_text=_('\'@\' characther not required.')
    )
    twitter_type = models.CharField(
        _('Resource type'), max_length=255, choices=meta_settings.TWITTER_TYPES, blank=True
    )
    gplus_author = models.CharField(
        _('Author Google+ URL'), max_length=255, default='', blank=True,
        help_text=_('Use the Google+ Name (together with "+")')
    )
    gplus_type = models.CharField(
        _('Resource type'), max_length=255, choices=meta_settings.GPLUS_TYPES, blank=True,
        help_text=_('Use Article for generic pages.')
    )

    class Meta:
        verbose_name = _('Page meta info (all languages)')
        verbose_name_plural = _('Page meta info (all languages)')

    def __str__(self):
        return _('Page Meta for {0}').format(self.extended_object)

    def copy_relations(self, oldinstance, language):
        for item in oldinstance.extra.all():
            if not item.__class__.objects.filter(
                attribute=item.attribute, name=item.name, value=item.value, page=self
            ).exists():
                item.pk = None
                item.page = self
                item.save()

extension_pool.register(PageMeta)


@python_2_unicode_compatible
class TitleMeta(TitleExtension):
    image = FilerFileField(
        null=True, blank=True, related_name='djangocms_page_meta_title',
        help_text=_('If empty, page image will be used for all languages.')
    )
    keywords = models.CharField(
        max_length=400, default='', blank=True
    )
    description = models.CharField(
        max_length=400, default='', blank=True
    )
    og_description = models.CharField(
        _('Facebook Description'), max_length=400, default='', blank=True
    )
    twitter_description = models.CharField(
        _('Twitter Description'), max_length=140, default='', blank=True
    )
    gplus_description = models.CharField(
        _('Google+ Description'), max_length=400, default='', blank=True
    )

    class Meta:
        verbose_name = _('Page meta info (language-dependent)')
        verbose_name_plural = _('Page meta info (language-dependent)')

    def __str__(self):
        return _('Title Meta for {0}').format(self.extended_object)

    @property
    def locale(self):
        if self.extended_object.language.find('_') > -1:
            return self.extended_object.language
        else:
            return None

    def copy_relations(self, oldinstance, language):
        for item in oldinstance.extra.all():
            item.pk = None
            item.title = self
            item.save()

extension_pool.register(TitleMeta)


@python_2_unicode_compatible
class GenericMetaAttribute(models.Model):
    DEFAULT_ATTRIBUTE = 'name'
    page = models.ForeignKey(PageMeta, null=True, blank=True, related_name='extra')
    title = models.ForeignKey(TitleMeta, null=True, blank=True, related_name='extra')
    attribute = models.CharField(
        _('attribute'), max_length=200, help_text=_('Custom attribute'), default='', blank=True,
    )
    name = models.CharField(
        _('name'), max_length=200, help_text=_('Meta attribute name'),
    )
    value = models.CharField(
        _('value'), max_length=2000, help_text=_('Meta attribute value'),
    )

    class Meta:
        verbose_name = _('Page meta info (language-dependent)')
        verbose_name_plural = _('Page meta info (language-dependent)')

    def __str__(self):
        if self.page:
            return _('Attribute {0} for page {1}').format(self.name, self.page)
        if self.title:
            return _('Attribute {0} for title {1}').format(self.name, self.title)


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
def cleanup_pagemeta(sender, instance, **kwargs):
    for language in instance.extended_object.get_languages():
        key = get_cache_key(instance.extended_object, language)
        cache.delete(key)


@receiver(post_save, sender=TitleMeta)
def cleanup_titlemeta(sender, instance, **kwargs):
    key = get_cache_key(instance.extended_object.page,
                        instance.extended_object.language)
    cache.delete(key)

if registry:
    registry.add_to_head(get_metatags)
