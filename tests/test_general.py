# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.cache import cache
from django.template.defaultfilters import slugify

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

    def atest_title_tags(self):
        """
        Tests the correct retrieval of tags for a title
        """
        page, page_2 = self.get_pages()

        # Assign and test english tags
        title_en = page.get_title_obj(language='en')
        title_en_tags = models.TitleTags.objects.create(extended_object=title_en)
        title_en_tags.tags.add(*self.tag_strings)

        self.assertTrue(title_has_tag(page, 'en', slugify(self.tag_strings[0])))
        self.assertTrue(title_has_tag(page, 'en', Tag.objects.get(slug=slugify(self.tag_strings[0]))))
        self.assertEqual(set(self.tag_strings), set([tag.name for tag in get_title_tags(page, 'en')]))

        # Assign and test french tags
        title_fr = page.get_title_obj(language='fr', fallback=False)
        title_fr_tags = models.TitleTags.objects.create(extended_object=title_fr)
        title_fr_tags.tags.add(*self.tag_strings_fr)
        self.assertTrue(title_has_tag(page, 'fr', slugify(self.tag_strings_fr[0])))
        self.assertEqual(set(self.tag_strings_fr), set([tag.name for tag in get_title_tags(page, 'fr')]))

        self.assertFalse(title_has_tag(page, 'it', slugify(self.tag_strings_fr[0])))
        self.assertEqual(set(), set([tag.name for tag in get_title_tags(page, 'it')]))

    def atest_tags_request_page(self):
        """
        Tests the correct retrieval of tags for a page  from request
        """
        page, page_2 = self.get_pages()

        # Assign tags to page
        page_meta = models.PageTags.objects.create(extended_object=page)
        page_meta.tags.add(*self.tag_strings)
        page.publish()

        cache.clear()
        # Reload page from request and extract tags from it
        request = self.get_request(page, 'en')
        with self.assertNumQueries(4):
            # 1st query to get the page for the key lookup
            # 2st query to get the page in get_page_meta_from_request
            # 3nd query to get the page extension
            # 4rd query to extract tags data
            tags_list = get_page_meta_from_request(request, page.get_public_object().pk, 'en', page.site_id)
        self.assertEqual(set(self.tag_strings), set([tag.name for tag in tags_list]))

        with self.assertNumQueries(1):
            # Second run executes exactly 1 query as data is fetched from cache
            # 1st query to get the page for the key lookup
            tags_list = get_page_meta_from_request(request, page.get_public_object().pk, 'en', page.site_id)

        # Empty page has no tags
        tags_list = get_page_meta_from_request(request, 40, 'en', 1)
        self.assertEqual(set(), set(tags_list))

    def atest_tags_request_title(self):
        """
        Tests the correct retrieval of tags for a title from request
        """
        page, page_2 = self.get_pages()

        # Assign tags to title
        title_tags = models.TitleTags.objects.create(extended_object=page.get_title_obj('en'))
        title_tags.tags.add(*self.tag_strings)
        page.publish()

        # Reload page from request and extract tags from it
        request = self.get_request(page, 'en')
        tags_list = get_title_tags_from_request(request, page.get_public_object().pk, 'en', page.site_id)
        self.assertEqual(set(self.tag_strings), set([tag.name for tag in tags_list]))
