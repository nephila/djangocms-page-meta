from copy import copy

from classytags.tests import DummyTokens
from django.conf import settings
from django.template.base import Parser
from django.test import override_settings
from django.utils.functional import SimpleLazyObject

from djangocms_page_meta import models
from djangocms_page_meta.forms import TitleMetaAdminForm
from djangocms_page_meta.templatetags.page_meta_tags import MetaFromPage
from djangocms_page_meta.utils import get_page_meta, meta_settings

from . import BaseTest


class PageMetaUtilsTest(BaseTest):

    def test_context_no_request(self):
        """
        This is a weird and limited test to ensure that if request is not in context
        no exception is thrown. In this case MetaFromPage.render_tag does not need
        a full environment to work
        """
        context = {}
        dummy_tokens = DummyTokens('myval', 'as', 'myname')
        tag = MetaFromPage.render_tag(MetaFromPage(Parser(dummy_tokens), dummy_tokens), context, None, 'meta')
        self.assertFalse(tag)
        self.assertTrue(context['meta'])

    def test_page_meta_og(self):
        """
        Tests the OpenGraph meta tags
        """
        page, _ = self.get_pages()
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
        self.assertEqual(meta.fb_pages, self.og_data['fb_pages'])
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
        page, _ = self.get_pages()
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
        page, _ = self.get_pages()
        page_meta = models.PageMeta.objects.create(extended_object=page)
        for key, val in self.page_data.items():
            setattr(page_meta, key, val)
        for key, val in self.gplus_data.items():
            setattr(page_meta, key, val)
        page_meta.save()

        page.reload()

        meta = get_page_meta(page, 'en')
        self.assertEqual(meta.gplus_author, 'https://plus.google.com/{0}'.format(self.gplus_data['gplus_author']))
        self.assertEqual(meta.gplus_type, self.gplus_data['gplus_type'])

        new_data = copy(self.gplus_data)
        new_data['gplus_author'] = 'https://plus.google.com/+SomeUser'
        for key, val in new_data.items():
            setattr(page_meta, key, val)
        page_meta.save()
        page.reload()
        meta = get_page_meta(page, 'en')
        self.assertEqual(meta.gplus_author, new_data['gplus_author'])

        new_data = copy(self.gplus_data)
        new_data['gplus_author'] = '/SomePage'
        for key, val in new_data.items():
            setattr(page_meta, key, val)
        page_meta.save()
        page.reload()
        meta = get_page_meta(page, 'en')
        self.assertEqual(meta.gplus_author, 'https://plus.google.com{0}'.format(new_data['gplus_author']))

    def test_page_meta_no_meta(self):
        """
        Tests the meta if no PageMeta is set
        """
        meta_settings.GPLUS_AUTHOR = self.gplus_data['gplus_author']
        page, _ = self.get_pages()

        meta = get_page_meta(page, 'en')
        self.assertEqual(
            meta.gplus_author, 'https://plus.google.com/{0}'.format(self.gplus_data['gplus_author'])
        )
        self.assertEqual(meta.gplus_type, self.gplus_data['gplus_type'])
        self.assertEqual(meta.published_time, page.publication_date.isoformat())
        self.assertEqual(meta.modified_time, page.changed_date.isoformat())
        meta_settings.GPLUS_AUTHOR = ''

    def test_none_page(self):
        meta = get_page_meta(None, 'en')
        self.assertIsNone(meta)

        request = self.get_page_request(SimpleLazyObject(lambda: None), self.user, '/')
        meta = get_page_meta(request.current_page, 'en')
        self.assertIsNone(meta)

    def test_tags(self):
        tags1 = ('pagetag.1', 'pagetag.2')
        tags2 = ('titletag.1', 'titletag.2')
        try:
            from djangocms_page_tags.models import PageTags, TitleTags
        except ImportError:
            self.skipTest('djangocms_page_tags not installed')
        page1, page2 = self.get_pages()
        page_ext = PageTags.objects.create(extended_object=page1)
        page_ext.tags.add(*tags1)
        title_ext = TitleTags.objects.create(extended_object=page1.get_title_obj('en'))
        title_ext.tags.add(*tags2)
        title_ext = TitleTags.objects.create(extended_object=page2.get_title_obj('en'))
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

        meta1 = get_page_meta(page1, 'en')
        meta2 = get_page_meta(page2, 'en')
        for tag in (tags2 + tags1):
            self.assertTrue(tag in meta1.tag)
        for tag in tags2:
            self.assertTrue(tag in meta2.tag)

    def test_custom_extra(self):
        page1, __ = self.get_pages()
        page_meta = models.PageMeta.objects.create(extended_object=page1)
        page_meta.save()
        title_meta = models.TitleMeta.objects.create(extended_object=page1.get_title_obj('en'))
        title_meta.save()

        models.GenericMetaAttribute.objects.create(
            page=page_meta, attribute='custom', name='attr', value='foo'
        )
        models.GenericMetaAttribute.objects.create(
            title=title_meta, attribute='custom', name='attr', value='bar'
        )

        page1.reload()

        meta = get_page_meta(page1, 'en')
        self.assertEqual(meta.extra_custom_props, [('custom', 'attr', 'bar'), ('custom', 'attr', 'foo')])

        meta = get_page_meta(page1, 'it')
        self.assertEqual(meta.extra_custom_props, [('custom', 'attr', 'foo')])

    def test_publish_extra(self):
        """
        Test that modified GenericMetaAttribute are not copied multiple times on page publish
        See issue #78
        """
        page1, __ = self.get_pages()
        page_meta = models.PageMeta.objects.create(extended_object=page1)
        title_meta = models.TitleMeta.objects.create(extended_object=page1.get_title_obj('en'))
        models.GenericMetaAttribute.objects.create(
            page=page_meta, attribute='custom', name='attr', value='foo'
        )
        models.GenericMetaAttribute.objects.create(
            title=title_meta, attribute='custom', name='attr', value='bar'
        )

        page1.publish('en')
        page_meta.extra.first().attribute = 'new'
        page_meta.extra.first().save()
        title_meta.extra.first().attribute = 'new'
        title_meta.extra.first().save()

        page1.publish('en')
        public = page1.get_public_object()
        page_meta = models.PageMeta.objects.get(extended_object=public)
        title_meta = models.TitleMeta.objects.get(extended_object=public.get_title_obj('en'))
        self.assertEqual(page_meta.extra.count(), 1)
        self.assertEqual(title_meta.extra.count(), 1)

    def test_form(self):
        page1, __ = self.get_pages()
        page_meta = models.PageMeta.objects.create(extended_object=page1)
        with override_settings(PAGE_META_DESCRIPTION_LENGTH=20, PAGE_META_TWITTER_DESCRIPTION_LENGTH=20):
            form = TitleMetaAdminForm(
                data={'description': 'major text over 20 characters long'},
                instance=page_meta
            )
            self.assertFalse(form.is_valid())
            form = TitleMetaAdminForm(
                data={'twitter_description': 'major text over 20 characters long'},
                instance=page_meta
            )
            self.assertFalse(form.is_valid())

            form = TitleMetaAdminForm(data={'description': 'mini text'}, instance=page_meta)
            self.assertTrue(form.is_valid())

            form = TitleMetaAdminForm(data={'twitter_description': 'mini text'}, instance=page_meta)
            self.assertTrue(form.is_valid())
