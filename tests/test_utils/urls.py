from cms.utils.conf import get_cms_setting
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path, re_path
from django.views.static import serve

admin.autodiscover()

urlpatterns = [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT, "show_indexes": True}),
    re_path(
        r"^media/cms/(?P<path>.*)$", serve, {"document_root": get_cms_setting("MEDIA_ROOT"), "show_indexes": True}
    ),
]

try:
    urlpatterns.insert(0, re_path(r"^admin/", admin.site.urls)),  # NOQA
except Exception:
    urlpatterns.insert(0, path("admin/", include(admin.site.urls))),  # NOQA

urlpatterns += staticfiles_urlpatterns()

urlpatterns += i18n_patterns(
    path("", include("cms.urls")),
)
