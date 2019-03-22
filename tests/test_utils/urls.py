# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.utils.conf import get_cms_setting
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

admin.autodiscover()

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'^media/cms/(?P<path>.*)$', serve,
        {'document_root': get_cms_setting('MEDIA_ROOT'), 'show_indexes': True}),
]

try:
    urlpatterns.insert(0, url(r'^admin/', admin.site.urls)),  # NOQA
except Exception:
    urlpatterns.insert(0, url(r'^admin/', include(admin.site.urls))),  # NOQA

urlpatterns += staticfiles_urlpatterns()

urlpatterns += i18n_patterns(
    url(r'^', include('cms.urls')),
)
