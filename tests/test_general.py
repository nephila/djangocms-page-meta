# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.functional import SimpleLazyObject
from djangocms_page_meta import models
from djangocms_page_meta.utils import get_page_meta

from . import BaseTest


class PageMetaUtilsTest(BaseTest):

    def test_page_meta_og(self):
        """
        Tests the OpenGraph meta tags
        """
        page, page_2 = self.get_pages()
        page_meta = models.PageMeta.objects.create(extended_object=page)
        for key, val in self.page_data.items():
            setattr(page_meta, key, val)
        for key, val in self.og_data.items():
            setattr(page_meta, key, val)
        page_meta.save()

        page.reload()

        meta = get_page_meta(page, 'en')
        self.assertEqual(meta.og_type, self.og_data['og_type'])
        self.assertEqual(meta.og_author_url, self.og_data['og_author_url'])
        self.assertEqual(meta.og_profile_id, self.og_data['og_author_fbid'])
        self.assertEqual(meta.og_publisher, self.og_data['og_publisher'])
        self.assertEqual(meta.og_app_id, self.og_data['og_app_id'])
        self.assertEqual(meta.published_time, page.publication_date.isoformat())
        self.assertEqual(meta.modified_time, page.changed_date.isoformat())
        if page.publication_end_date:
            self.assertEqual(meta.expiration_time, page.publication_end_date.isoformat())
        else:
            self.assertFalse(hasattr(meta, 'expiration_time'))

    def test_page_meta_twitter(self):
        """
        Tests the Twitter cards
        """
        page, page_2 = self.get_pages()
        page_meta = models.PageMeta.objects.create(extended_object=page)
        for key, val in self.page_data.items():
            setattr(page_meta, key, val)
        for key, val in self.twitter_data.items():
            setattr(page_meta, key, val)
        page_meta.save()

        page.reload()

        meta = get_page_meta(page, 'en')
        self.assertEqual(meta.twitter_site, self.twitter_data['twitter_site'])
        self.assertEqual(meta.twitter_author, self.twitter_data['twitter_author'])
        self.assertEqual(meta.twitter_type, self.twitter_data['twitter_type'])
        self.assertEqual(meta.get_domain(), settings.META_SITE_DOMAIN)

    def test_page_meta_gplus(self):
        """
        Tests the Google+ schema data
        """
        page, page_2 = self.get_pages()
        page_meta = models.PageMeta.objects.create(extended_object=page)
        for key, val in self.page_data.items():
            setattr(page_meta, key, val)
        for key, val in self.gplus_data.items():
            setattr(page_meta, key, val)
        page_meta.save()

        page.reload()

        meta = get_page_meta(page, 'en')
        self.assertEqual(meta.gplus_author, self.gplus_data['gplus_author'])
        self.assertEqual(meta.gplus_type, self.gplus_data['gplus_type'])

    def test_none_page(self):
        meta = get_page_meta(None, 'en')
        self.assertIsNone(meta)

        request = self.get_page_request(SimpleLazyObject(lambda: None), self.user, '/')
        meta = get_page_meta(request.current_page, 'en')
        self.assertIsNone(meta)
