# -*- coding: utf-8 -*-

from aldryn_client import forms


class Form(forms.BaseForm):

    META_SITE_PROTOCOL = forms.CharField('META_SITE_PROTOCOL', required=False)
    META_SITE_DOMAIN = forms.CharField('META_SITE_DOMAIN', required=False)
    META_SITE_TYPE = forms.CharField('META_SITE_TYPE', required=False)
    META_SITE_NAME = forms.CharField('META_SITE_NAME', required=False)
    META_INCLUDE_KEYWORDS = forms.CharField('META_INCLUDE_KEYWORDS', required=False)
    META_DEFAULT_KEYWORDS = forms.CharField('META_DEFAULT_KEYWORDS', required=False)
    META_IMAGE_URL = forms.CharField('META_IMAGE_URL', required=False)
    META_USE_OG_PROPERTIES = forms.CheckboxField('META_USE_OG_PROPERTIES', required=False)
    META_USE_TWITTER_PROPERTIES = forms.CheckboxField('META_USE_TWITTER_PROPERTIES', required=False)
    META_USE_GOOGLEPLUS_PROPERTIES = forms.CheckboxField('META_USE_GOOGLEPLUS_PROPERTIESS', required=False)
    META_USE_TITLE_TAG = forms.CheckboxField('META_USE_TITLE_TAG', required=False)
    META_USE_SITES = forms.CheckboxField('META_USE_SITES', required=False)

    def to_settings(self, data, settings):
        settings['META_SITE_PROTOCOL'] = data['META_SITE_PROTOCOL']
        settings['META_SITE_DOMAIN'] = data['META_SITE_DOMAIN']
        settings['META_SITE_TYPE'] = data['META_SITE_TYPE']
        settings['META_INCLUDE_KEYWORDS'] = data['META_INCLUDE_KEYWORDS']
        settings['META_IMAGE_URL'] = data['META_IMAGE_URL']
        settings['META_USE_OG_PROPERTIES'] = data['META_USE_OG_PROPERTIES']
        settings['META_USE_TWITTER_PROPERTIES'] = data['META_USE_TWITTER_PROPERTIES']
        settings['META_USE_GOOGLEPLUS_PROPERTIES'] = data['META_USE_GOOGLEPLUS_PROPERTIES']
        settings['META_USE_TITLE_TAG'] = data['META_USE_TITLE_TAG']
        settings['META_USE_SITES'] = data['META_USE_SITES']
        return settings