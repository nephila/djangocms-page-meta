# -*- coding: utf-8 -*-
from aldryn_client import forms


OBJECT_TYPES = (
    ('', '----'),
    ('Article', 'Article'),
    ('Website', 'Website'),
)

PROTOCOLS = (
    ('', '----'),
    ('http', 'http'),
    ('https', 'https'),
)


class Form(forms.BaseForm):

    META_SITE_PROTOCOL = forms.SelectField(
        'Site protocol',
        choices=PROTOCOLS,
        required=False
    )
    META_SITE_TYPE = forms.SelectField(
        'Site type',
        choices=OBJECT_TYPES,
        required=False
    )
    META_SITE_NAME = forms.CharField('Site name', required=False)
    META_USE_OG_PROPERTIES = forms.CheckboxField(
        'Render the OpenGraph properties',
        required=False
    )
    META_USE_TWITTER_PROPERTIES = forms.CheckboxField(
        'Render the Twitter properties',
        required=False
    )
    META_USE_GOOGLEPLUS_PROPERTIES = forms.CheckboxField(
        'Render the Google properties',
        required=False
    )

    def to_settings(self, data, settings):
        settings['META_SITE_PROTOCOL'] = data['META_SITE_PROTOCOL']
        settings['META_SITE_TYPE'] = data['META_SITE_TYPE']
        settings['META_SITE_NAME'] = data['META_SITE_NAME']
        settings['META_INCLUDE_KEYWORDS'] = []
        settings['META_DEFAULT_KEYWORDS'] = []
        settings['META_USE_OG_PROPERTIES'] = data['META_USE_OG_PROPERTIES']
        settings['META_USE_TWITTER_PROPERTIES'] = data['META_USE_TWITTER_PROPERTIES']
        settings['META_USE_GOOGLEPLUS_PROPERTIES'] = data['META_USE_GOOGLEPLUS_PROPERTIES']
        settings['META_USE_TITLE_TAG'] = False
        settings['META_USE_SITES'] = True
        return settings
