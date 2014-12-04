# -*- coding: utf-8 -*-
from cms.extensions import PageExtensionAdmin, TitleExtensionAdmin
from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .forms import TitleMetaAdminForm
from .models import PageMeta, TitleMeta


class PageMetaAdmin(PageExtensionAdmin):
    raw_id_fields = ('og_author',)
    fieldsets = (
        (None, {'fields': ('image',)}),
        (_(u'OpenGraph'), {'fields': ('og_type',
                                      ('og_author', 'og_author_url', 'og_author_fbid'),
                                      ('og_publisher', 'og_app_id')),
                           'classes': ('collapse',)}),
        (_(u'Twitter Cards'), {'fields': ('twitter_type', 'twitter_author'),
                               'classes': ('collapse',)}),
        (_(u'Google+ Snippets'), {'fields': ('gplus_type', 'gplus_author'),
                                  'classes': ('collapse',)}),
    )

    class Media:
        css = {
            'all': ('%sdjangocms_page_meta/css/%s' % (
                settings.STATIC_URL, "djangocms_page_meta_admin.css"),)
        }

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

admin.site.register(PageMeta, PageMetaAdmin)


class TitleMetaAdmin(TitleExtensionAdmin):
    form = TitleMetaAdminForm

    class Media:
        css = {
            'all': ('%sdjangocms_page_meta/css/%s' % (
                settings.STATIC_URL, "djangocms_page_meta_admin.css"),)
        }

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

admin.site.register(TitleMeta, TitleMetaAdmin)
