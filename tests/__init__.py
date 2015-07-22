# -*- coding: utf-8 -*-
from djangocms_helper.base_test import BaseTestCase


class BaseTest(BaseTestCase):
    """
    Base class with utility function
    """
    page_data = {}
    _pages_data = (
        {'en': {'title': 'page one', 'template': 'page_meta.html', 'publish': True},
         'fr_FR': {'title': 'page un', 'publish': True},
         'it': {'title': 'pagina uno', 'publish': True}},
        {'en': {'title': 'page two', 'template': 'page_meta.html', 'publish': True},
         'fr_FR': {'title': 'page deux', 'publish': True},
         'it': {'title': 'pagina due', 'publish': True}},
    )
    title_data = {
        'keywords': 'keyword1, keyword2, keyword3',
        'description': 'base lorem ipsum - english',
        'og_description': 'opengraph - lorem ipsum - english',
        'twitter_description': 'twitter - lorem ipsum - english',
        'gplus_description': 'gplus - lorem ipsum - english',
    }
    title_data_it = {
        'keywords': 'parola1, parola2, parola3',
        'description': 'base lorem ipsum - italian',
        'og_description': 'opengraph - lorem ipsum - italian',
        'twitter_description': 'twitter - lorem ipsum - italian',
        'gplus_description': 'gplus - lorem ipsum - italian',
    }
    og_data = {
        'og_type': 'article',
        'og_author_url': 'https://facebook.com/FakeUser',
        'og_author_fbid': u'123456789',
        'og_publisher': 'https://facebook.com/FakeUser',
        'og_app_id': u'123456789',
    }
    twitter_data = {
        'twitter_author': 'fake_user',
        'twitter_site': 'fake_site',
        'twitter_type': 'summary',
    }
    gplus_data = {
        'gplus_author': '+FakeUser',
        'gplus_type': 'Article',
    }
