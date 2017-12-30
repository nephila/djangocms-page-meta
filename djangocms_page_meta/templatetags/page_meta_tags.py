# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from classytags.arguments import Argument
from classytags.core import Options, Tag
from cms.utils import get_language_from_request
from django import template
from meta.views import Meta

from ..utils import get_page_meta

register = template.Library()


@register.tag(name='page_meta')
class MetaFromPage(Tag):
    name = 'page_meta'
    options = Options(
        Argument('page'),
        'as',
        Argument('varname', required=True, resolve=False),
    )

    def render_tag(self, context, page, varname):
        request = context.get('request')
        if request:
            language = get_language_from_request(request)
            meta = get_page_meta(page, language)
        else:
            meta = Meta()
        context[varname] = meta
        return ''
