from django.conf import settings
from django.core.cache import cache
from django.template.base import Parser
from django.test import override_settings
from django.utils.functional import SimpleLazyObject

from djangocms_page_meta import models
from djangocms_page_meta.forms import TitleMetaAdminForm
from djangocms_page_meta.templatetags.page_meta_tags import MetaFromPage
from djangocms_page_meta.utils import get_cache_key, get_page_meta

from . import BaseTest, DummyTokens


class PageMetaUtilsTest(BaseTest):
    def test_context_no_request(self):
        """
        This is a weird and limited test to ensure that if request is not in context
        no exception is thrown. In this case MetaFromPage.render_tag does not need
        a full environment to work
        """
        context = {}
        dummy_tokens = DummyTokens("myval", "as", "myname")
        tag = MetaFromPage.render_tag(MetaFromPage(Parser(dummy_tokens), dummy_tokens), context, None, "meta")
        self.assertFalse(tag)
        self.assertTrue(context["meta"])

    def test_page_meta_og(self):
        """
        Tests the OpenGraph meta tags
        """
        page, __ = self.get_pages()
        page_meta = models.PageMeta.objects.create(extended_object=page)
        for key, val in self.page_data.items():
            setattr(page_meta, key, val)
        for key, val in self.og_data.items():
            setattr(page_meta, key, val)
        page_meta.save()

        page.reload()

        meta = get_page_meta(page, "en")
        self.assertEqual(meta.og_type, self.og_data["og_type"])
        self.assertEqual(meta.og_author_url, self.og_data["og_author_url"])
        self.assertEqual(meta.og_profile_id, self.og_data["og_author_fbid"])
        self.assertEqual(meta.og_publisher, self.og_data["og_publisher"])
        self.assertEqual(meta.og_app_id, self.og_data["og_app_id"])
        self.assertEqual(meta.fb_pages, self.og_data["fb_pages"])
        self.assertEqual(meta.published_time, page.publication_date.isoformat())
        self.assertEqual(meta.modified_time, page.changed_date.isoformat())
        if page.publication_end_date:
            self.assertEqual(meta.expiration_time, page.publication_end_date.isoformat())
        else:
            self.assertFalse(hasattr(meta, "expiration_time"))

    def test_page_meta_twitter(self):
        """
        Tests the Twitter cards
        """
        page, __ = self.get_pages()
        page_meta = models.PageMeta.objects.create(extended_object=page)
        for key, val in self.page_data.items():
            setattr(page_meta, key, val)
        for key, val in self.twitter_data.items():
            setattr(page_meta, key, val)
        page_meta.save()

        page.reload()

        meta = get_page_meta(page, "en")
        self.assertEqual(meta.twitter_site, self.twitter_data["twitter_site"])
        self.assertEqual(meta.twitter_author, self.twitter_data["twitter_author"])
        self.assertEqual(meta.twitter_type, self.twitter_data["twitter_type"])
        self.assertEqual(meta.get_domain(), settings.META_SITE_DOMAIN)

    def test_none_page(self):
        meta = get_page_meta(None, "en")
        self.assertIsNone(meta)

        request = self.get_page_request(SimpleLazyObject(lambda: None), self.user, "/")
        meta = get_page_meta(request.current_page, "en")
        self.assertIsNone(meta)

    def test_tags(self):
        tags1 = ("pagetag.1", "pagetag.2")
        tags2 = ("titletag.1", "titletag.2")
        try:
            from djangocms_page_tags.models import PageTags, TitleTags
        except ImportError:
            self.skipTest("djangocms_page_tags not installed")
        page1, page2 = self.get_pages()
        page_ext = PageTags.objects.create(extended_object=page1)
        page_ext.tags.add(*tags1)
        title_ext = TitleTags.objects.create(extended_object=page1.get_title_obj("en"))
        title_ext.tags.add(*tags2)
        title_ext = TitleTags.objects.create(extended_object=page2.get_title_obj("en"))
        title_ext.tags.add(*tags2)

        for page in (page1, page2):
            page_meta = models.PageMeta.objects.create(extended_object=page)
            for key, val in self.page_data.items():
                setattr(page_meta, key, val)
            for key, val in self.og_data.items():
                setattr(page_meta, key, val)
            page_meta.save()
            page.reload()

        for lang in self.languages:
            page1.publish(lang)
            page2.publish(lang)
        page1 = page1.get_public_object()
        page2 = page2.get_public_object()

        meta1 = get_page_meta(page1, "en")
        meta2 = get_page_meta(page2, "en")
        for tag in tags2 + tags1:
            self.assertTrue(tag in meta1.tag)
        for tag in tags2:
            self.assertTrue(tag in meta2.tag)

    def test_custom_extra(self):
        page1, __ = self.get_pages()
        page_meta = models.PageMeta.objects.create(extended_object=page1)
        page_meta.save()
        title_meta = models.TitleMeta.objects.create(extended_object=page1.get_title_obj("en"))
        title_meta.save()

        models.GenericMetaAttribute.objects.create(page=page_meta, attribute="custom", name="attr", value="foo")
        models.GenericMetaAttribute.objects.create(title=title_meta, attribute="custom", name="attr", value="bar")

        page1.reload()

        meta = get_page_meta(page1, "en")
        self.assertEqual(meta.extra_custom_props, [("custom", "attr", "bar"), ("custom", "attr", "foo")])

        meta = get_page_meta(page1, "it")
        self.assertEqual(meta.extra_custom_props, [("custom", "attr", "foo")])

    def test_publish_extra(self):
        """
        Test that modified GenericMetaAttribute are not copied multiple times on page publish
        See issue #78
        """
        page1, __ = self.get_pages()
        page_meta = models.PageMeta.objects.create(extended_object=page1)
        title_meta = models.TitleMeta.objects.create(extended_object=page1.get_title_obj("en"))
        models.GenericMetaAttribute.objects.create(page=page_meta, attribute="custom", name="attr", value="foo")
        models.GenericMetaAttribute.objects.create(title=title_meta, attribute="custom", name="attr", value="bar")

        page1.publish("en")
        page_meta.extra.first().attribute = "new"
        page_meta.extra.first().save()
        title_meta.extra.first().attribute = "new"
        title_meta.extra.first().save()

        page1.publish("en")
        public = page1.get_public_object()
        page_meta = models.PageMeta.objects.get(extended_object=public)
        title_meta = models.TitleMeta.objects.get(extended_object=public.get_title_obj("en"))
        self.assertEqual(page_meta.extra.count(), 1)
        self.assertEqual(title_meta.extra.count(), 1)

    def test_str_methods(self):
        """
        Models str are created
        """
        page1, __ = self.get_pages()
        page_meta = models.PageMeta.objects.create(extended_object=page1)
        title_meta = models.TitleMeta.objects.create(extended_object=page1.get_title_obj("en"))
        page_attr = models.GenericMetaAttribute.objects.create(
            page=page_meta, attribute="custom", name="attr", value="foo"
        )
        title_attr = models.GenericMetaAttribute.objects.create(
            title=title_meta, attribute="custom", name="attr", value="bar"
        )

        self.assertEqual(str(page_meta), f"Page Meta for {page1}")
        self.assertEqual(str(title_meta), f"Title Meta for {page1.get_title_obj('en')}")
        self.assertEqual(str(page_attr), f"Attribute {page_attr.name} for {page_meta}")
        self.assertEqual(str(title_attr), f"Attribute {title_attr.name} for {title_meta}")

    def test_cache_cleanup_on_update_delete_meta(self):
        """
        Meta caches are emptied when updating / deleting a meta
        """
        page1, __ = self.get_pages()
        page_meta = models.PageMeta.objects.create(extended_object=page1)
        title_meta = models.TitleMeta.objects.create(extended_object=page1.get_title_obj("en"))

        # cache objects
        for language in page1.get_languages():
            get_page_meta(page1, language)
        title_key = get_cache_key(title_meta.extended_object.page, title_meta.extended_object.language)
        self.assertTrue(cache.get(title_key))

        # Title update check
        title_meta.description = "Something"
        title_meta.save()
        self.assertIsNone(cache.get(title_key))

        # Refreshing cache
        get_page_meta(page1, title_meta.extended_object.language)
        self.assertTrue(cache.get(title_key))

        # Page update check
        page_meta.og_author_url = "Something"
        page_meta.save()
        self.assertIsNone(cache.get(title_key))

        # Refreshing cache
        get_page_meta(page1, title_meta.extended_object.language)
        self.assertTrue(cache.get(title_key))

        # Check deleting objects
        title_meta.delete()
        self.assertIsNone(cache.get(title_key))

        page_meta.delete()
        for language in page1.get_languages():
            title_key = get_cache_key(page1, language)
            self.assertIsNone(cache.get(title_key))

    def test_cache_cleanup_on_update_delete_page(self):
        """
        Meta caches are emptied when deleting a page.
        """
        page1, __ = self.get_pages()
        page_meta = models.PageMeta.objects.create(extended_object=page1)
        title_meta = models.TitleMeta.objects.create(extended_object=page1.get_title_obj("en"))

        # cache objects - cache keys must be pre calculated as the page will not exist anymore when running the
        # asserts
        meta_cache_keys = []
        for language in page1.get_languages():
            get_page_meta(page1, language)
            meta_cache_keys.append(get_cache_key(page1, language))
        title_key = get_cache_key(title_meta.extended_object.page, title_meta.extended_object.language)
        self.assertTrue(cache.get(title_key))

        # Check deleting objects
        title_meta.extended_object.delete()
        self.assertIsNone(cache.get(title_key))

        page_meta.delete()
        for title_key in meta_cache_keys:
            self.assertIsNone(cache.get(title_key))

    def test_form(self):
        page1, __ = self.get_pages()
        page_meta = models.PageMeta.objects.create(extended_object=page1)
        with override_settings(PAGE_META_DESCRIPTION_LENGTH=20, PAGE_META_TWITTER_DESCRIPTION_LENGTH=20):
            form = TitleMetaAdminForm(data={"description": "major text over 20 characters long"}, instance=page_meta)
            self.assertFalse(form.is_valid())
            form = TitleMetaAdminForm(
                data={"twitter_description": "major text over 20 characters long"}, instance=page_meta
            )
            self.assertFalse(form.is_valid())

            form = TitleMetaAdminForm(data={"description": "mini text"}, instance=page_meta)
            self.assertTrue(form.is_valid())

            form = TitleMetaAdminForm(data={"twitter_description": "mini text"}, instance=page_meta)
            self.assertTrue(form.is_valid())
