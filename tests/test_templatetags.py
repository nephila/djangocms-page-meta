# -*- coding: utf-8 -*-
from cms.views import details
from django.contrib.auth.models import AnonymousUser
from datetime import timedelta

from djangocms_page_meta.models import PageMeta, TitleMeta

from . import BaseTest


class TemplateMetaTest(BaseTest):

    def test_page_meta(self):
        """
        Test page-level templatetags
        """
        page1, page2 = self.get_pages()
        page_ext = PageMeta.objects.create(extended_object=page1)
        for key, val in self.og_data.items():
            setattr(page_ext, key, val)
        page_ext.save()
        page1.publication_end_date = page1.publication_date + timedelta(days=1)
        page1.publish('it')
        page1.publish('en')

        response = self.client.get("/en/")
        self.assertContains(response, '<meta name="twitter:domain" content="example.com">')
        self.assertContains(response, '<meta itemprop="datePublished" content="%s">' % page1.publication_date.isoformat())
        self.assertContains(response, '<meta property="article:expiration_time" content="%s">' % page1.publication_end_date.isoformat())
        self.assertContains(response, '<meta property="article:publisher" content="https://facebook.com/FakeUser">')

    def test_title_meta(self):
        """
        Test title-level templatetags
        """
        page1, page2 = self.get_pages()
        title_en = page1.get_title_obj(language='en', fallback=False)
        title_it = page1.get_title_obj(language='it', fallback=False)
        title_ext = TitleMeta.objects.create(extended_object=title_en)
        for key, val in self.title_data.items():
            setattr(title_ext, key, val)
        title_ext.save()
        title_ext = TitleMeta.objects.create(extended_object=title_it)
        for key, val in self.title_data_it.items():
            setattr(title_ext, key, val)
        title_ext.save()
        page1.publish('it')
        page1.publish('en')

        # Italian language
        response = self.client.get("/it/")
        response.render()
        self.assertContains(response, '<meta itemprop="description" content="lorem ipsum - italian">')
        self.assertContains(response, '<meta property="og:title" content="pagina uno">')
        self.assertContains(response, '<meta property="og:url" content="http://example.com/it/">')

        # English language
        response = self.client.get("/en/")
        self.assertContains(response, '<meta itemprop="description" content="lorem ipsum - english">')
        self.assertContains(response, '<meta property="og:title" content="page one">')
        self.assertContains(response, '<meta property="og:url" content="http://example.com/en/">')
