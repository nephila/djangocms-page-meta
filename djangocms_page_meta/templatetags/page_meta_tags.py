# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from classytags.arguments import Argument
from classytags.core import Options, Tag
from cms.utils import get_language_from_request
from django import template

from ..utils import get_page_meta

register = template.Library()


class MetaFromPage(Tag):
    name = 'page_meta'
    options = Options(
        Argument('page'),
        'as',
        Argument('varname', required=True, resolve=False),
    )

    def render_tag(self, context, page, varname):
        language = get_language_from_request(context['request'])
        meta = get_page_meta(page, language)
        context[varname] = meta
        return ''
register.tag(MetaFromPage)
