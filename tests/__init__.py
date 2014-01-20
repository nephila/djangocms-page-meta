# -*- coding: utf-8 -*-
"""
Tests for `djangocms_page_meta` module.
"""
from cms.utils.i18n import get_language_list

from django.contrib.auth.models import User
from django.http import SimpleCookie
from django.test import TestCase, RequestFactory
from six import StringIO
from cms.models import Page
from djangocms_page_meta.models import TitleMeta, PageMeta


class BaseTest(TestCase):
    """
    Base class with utility function
    """
    request_factory = None
    user = None
    languages = get_language_list()
    page_data = {
    }
    title_data = {
        'keywords': 'keyword1, keyword2, keyword3',
        'description': 'lorem ipsum - english',
    }
    title_data_it = {
        'keywords': 'parola1, parola2, parola3',
        'description': 'lorem ipsum - italian',
    }
    og_data = {
        'og_type': 'article',
        'og_author_url': 'https://facebook.com/FakeUser',
        'og_author_fbid': 123456789,
        'og_publisher': 'https://facebook.com/FakeUser',
        'og_app_id': 123456789,
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

    @classmethod
    def setUpClass(cls):
        cls.request_factory = RequestFactory()
        cls.user = User.objects.create(username='admin', is_staff=True, is_superuser=True)
        cls.user_staff = User.objects.create(username='staff', is_staff=True)
        cls.user_normal = User.objects.create(username='normal')

    def get_pages(self):
        from cms.api import create_page, create_title
        page = create_page(u'page one', 'page.html', language='en')
        page_2 = create_page(u'page two', 'page.html', language='en')
        create_title(language='fr_FR', title=u'page un', page=page)
        create_title(language='it', title=u'pagina uno', page=page)
        page.publish()
        page_2.publish()
        return page.get_draft_object(), page_2.get_draft_object()

    def get_request(self, page, lang):
        request = self.request_factory.get(page.get_path(lang))
        request.current_page = page
        request.user = self.user
        request.session = {}
        request.cookies = SimpleCookie()
        request.errors = StringIO()
        request.LANGUAGE_CODE = lang
        return request

    def get_page_request(self, page, user, path=None, edit=False, lang_code='en'):
        from cms.middleware.toolbar import ToolbarMiddleware
        path = path or page and page.get_absolute_url(lang_code)
        if edit:
            path += '?edit'
        request = RequestFactory().get(path)
        request.session = {}
        request.user = user
        request.LANGUAGE_CODE = lang_code
        if edit:
            request.GET = {'edit': None}
        else:
            request.GET = {'edit_off': None}
        request.current_page = page
        mid = ToolbarMiddleware()
        mid.process_request(request)
        return request

    def tearDown(self):
        Page.objects.all().delete()
        PageMeta.objects.all().delete()
        TitleMeta.objects.all().delete()

    @classmethod
    def tearDownClass(cls):
        User.objects.all().delete()
