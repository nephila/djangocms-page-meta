# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.utils.translation import ugettext_lazy as _


def get_setting(name):
    from django.conf import settings

    description_length = getattr(
        settings, 'PAGE_META_DESCRIPTION_LENGTH', None
    ) or 320

    tw_description_length = getattr(
        settings, 'PAGE_META_TWITTER_DESCRIPTION_LENGTH', None
    ) or 320

    robots_choices = getattr(
        settings, 'PAGE_META_ROBOTS_CHOICES', None
    ) or (
        ('none', _('none')),
        ('noindex', _('noindex')),
        ('noimageindex', _('noimageindex')),
        ('nofollow', _('nofollow')),
        ('nosnippet', _('nosnippet')),
        ('noarchive', _('noarchive')),
        ('notranslate', _('notranslate')),
    )

    default = {
        'PAGE_META_DESCRIPTION_LENGTH': description_length,
        'PAGE_META_TWITTER_DESCRIPTION_LENGTH': tw_description_length,
        'PAGE_META_ROBOTS_CHOICES': robots_choices,
    }
    return default['PAGE_META_%s' % name]
