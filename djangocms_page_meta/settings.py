# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals


def get_setting(name):
    from django.conf import settings

    default = {
        'PAGE_META_DESCRIPTION_LENGTH': getattr(
            settings, 'PAGE_META_DESCRIPTION_LENGTH', 320
        ),
        'PAGE_META_TWITTER_DESCRIPTION_LENGTH': getattr(
            settings, 'PAGE_META_TWITTER_DESCRIPTION_LENGTH', 280
        ),
    }
    return default['PAGE_META_%s' % name]
