#!/usr/bin/env python
from tempfile import mkdtemp


def gettext(s): return s  # NOQA


HELPER_SETTINGS = dict(
    NOSE_ARGS=[
        '-s',
    ],
    ROOT_URLCONF='tests.test_utils.urls',
    INSTALLED_APPS=[
        'easy_thumbnails',
        'filer',
        'taggit',
        'taggit_autosuggest',
        'meta',
        'djangocms_page_tags',
        'tests.test_utils',
    ],
    LANGUAGE_CODE='en',
    LANGUAGES=(
        ('en', gettext('English')),
        ('fr-fr', gettext('French')),
        ('it', gettext('Italiano')),
    ),
    CMS_LANGUAGES={
        1: [
            {
                'code': 'en',
                'name': gettext('English'),
                'public': True,
            },
            {
                'code': 'it',
                'name': gettext('Italiano'),
                'public': True,
            },
            {
                'code': 'fr-fr',
                'name': gettext('French'),
                'public': True,
            },
        ],
        'default': {
            'hide_untranslated': False,
        },
    },
    CMS_TEMPLATES=(
        ('page_meta.html', 'page'),
    ),
    META_SITE_PROTOCOL='http',
    META_SITE_DOMAIN='example.com',
    META_USE_OG_PROPERTIES=True,
    META_USE_TWITTER_PROPERTIES=True,
    META_USE_GOOGLEPLUS_PROPERTIES=True,
    THUMBNAIL_PROCESSORS=(
        'easy_thumbnails.processors.colorspace',
        'easy_thumbnails.processors.autocrop',
        'filer.thumbnail_processors.scale_and_crop_with_subject_location',
        'easy_thumbnails.processors.filters',
    ),
    FILE_UPLOAD_TEMP_DIR=mkdtemp(),
)


def run():
    from djangocms_helper import runner
    runner.cms('djangocms_page_meta')


def setup():
    import sys
    from djangocms_helper import runner
    runner.setup('djangocms_page_meta', sys.modules[__name__], use_cms=True)


if __name__ == '__main__':
    run()
