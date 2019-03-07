# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals


def get_setting(name):
    from django.conf import settings

    description_length = getattr(
        settings, 'PAGE_META_DESCRIPTION_LENGTH', None
    )
    if not description_length:
        description_length = 320

    tw_description_length = getattr(
        settings, 'PAGE_META_TWITTER_DESCRIPTION_LENGTH', None
    )
    if not tw_description_length:
        tw_description_length = 280

    default = {
        'PAGE_META_DESCRIPTION_LENGTH': description_length,
        'PAGE_META_TWITTER_DESCRIPTION_LENGTH': tw_description_length,
    }
    return default['PAGE_META_%s' % name]
