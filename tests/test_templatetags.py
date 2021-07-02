from datetime import timedelta

from djangocms_page_meta.models import GenericMetaAttribute, PageMeta, TitleMeta

from cms.api import create_page

from . import BaseTest


class TemplateMetaTest(BaseTest):
    def test_page_meta(self):
        """
        Test page-level templatetags
        """
        language = "en"
        page = create_page(title='test', template="page_meta.html", language=language)
        page_ext = PageMeta.objects.create(extended_object=page)
        for key, val in self.og_data.items():
            setattr(page_ext, key, val)
        page_ext.save()

        GenericMetaAttribute.objects.create(page=page_ext, attribute="custom", name="attr", value="foo")
        page.publication_end_date = page.creation_date + timedelta(days=1)
        page.published_date = page.changed_date
        page.save()
        page_url = page.get_absolute_url(language)

        with self.login_user_context(self.user):
            response = self.client.get(page_url)
        self.assertContains(response, '<meta name="twitter:domain" content="example.com">')
        self.assertContains(response, '<meta property="article:publisher" content="https://facebook.com/FakeUser">')
        self.assertContains(response, '<meta custom="attr" content="foo">')

    def test_title_meta(self):
        """
        Test title-level templatetags
        """
        page_en = create_page(title='test en', template="page_meta.html", language='en')
        page_it = create_page(title='test it', template="page_meta.html", language='it')
        title_en = page_en.get_title_obj(language="en", fallback=False)
        title_it = page_it.get_title_obj(language="it", fallback=False)
        title_ext = TitleMeta.objects.create(extended_object=title_en)
        for key, val in self.title_data.items():
            setattr(title_ext, key, val)
        title_ext.save()
        GenericMetaAttribute.objects.create(title=title_ext, attribute="custom", name="attr", value="foo-en")
        title_ext = TitleMeta.objects.create(extended_object=title_it)
        for key, val in self.title_data_it.items():
            setattr(title_ext, key, val)
        title_ext.save()
        GenericMetaAttribute.objects.create(title=title_ext, attribute="custom", name="attr", value="foo-it")

        # Italian language
        page_url_it = page_it.get_absolute_url('it')

        with self.login_user_context(self.user):
            response = self.client.get(page_url_it)

        self.assertContains(response, '<meta name="twitter:description" content="twitter - lorem ipsum - italian">')
        self.assertContains(response, '<meta itemprop="description" content="gplus - lorem ipsum - italian">')
        self.assertContains(response, '<meta property="og:description" content="opengraph - lorem ipsum - italian">')
        self.assertContains(response, '<meta property="og:title" content="test it">')
        self.assertContains(
             response, '<meta property="og:url" content="http://example.com%s">' % page_it.get_absolute_url("it")
        )
        self.assertContains(response, '<meta custom="attr" content="foo-it">')

        # English language
        page_url_en = page_en.get_absolute_url('en')

        with self.login_user_context(self.user):
            response = self.client.get(page_url_en)
        self.assertContains(response, '<meta name="twitter:description" content="twitter - lorem ipsum - english">')
        self.assertContains(response, '<meta itemprop="description" content="gplus - lorem ipsum - english">')
        self.assertContains(response, '<meta property="og:description" content="opengraph - lorem ipsum - english">')
        self.assertContains(response, '<meta property="og:title" content="test en">')
        self.assertContains(
            response, '<meta property="og:url" content="http://example.com%s">' % page_en.get_absolute_url('en')
        )
        self.assertContains(response, '<meta custom="attr" content="foo-en">')

    def test_fallbacks(self):
        """
        Test title-level templatetags
        """
        page1 = create_page(title='page one', template="page_meta.html", language='en')
        page2 = create_page(title='page two', template="page_meta.html", language='en')
        page_it = create_page(title='page it', template="page_meta.html", language='it')
        title_en = page1.get_title_obj(language="en", fallback=False)
        title_en.meta_description = self.title_data["description"]
        title_en.save()

        title_it = page_it.get_title_obj(language="it", fallback=False)
        title_it.meta_description = self.title_data_it["description"]
        title_it.save()

        title_ext_en = TitleMeta.objects.create(extended_object=title_en)
        title_ext_en.save()
        title_ext_it = TitleMeta.objects.create(extended_object=title_it)
        title_ext_it.save()

        title_en = page1.get_title_obj(language="en", fallback=False)
        title_ext_en = title_en.titlemeta

        # Italian language
        page_url_it = page_it.get_absolute_url('it')
        with self.login_user_context(self.user):
            response = self.client.get(page_url_it)
        # response.render()
        self.assertContains(response, '<meta name="description" content="base lorem ipsum - italian">')
        self.assertContains(response, '<meta name="twitter:description" content="base lorem ipsum - italian">')
        self.assertContains(response, '<meta itemprop="description" content="base lorem ipsum - italian">')
        self.assertContains(response, '<meta property="og:description" content="base lorem ipsum - italian">')
        self.assertContains(response, '<meta property="og:title" content="page it">')
        self.assertContains(
            response, '<meta property="og:url" content="http://example.com%s">' % page_it.get_absolute_url("it")
        )

        # English language
        page_url_en = page1.get_absolute_url('en')
        with self.login_user_context(self.user):
            response = self.client.get(page_url_en)
        self.assertContains(response, '<meta name="description" content="base lorem ipsum - english">')
        self.assertContains(response, '<meta name="twitter:description" content="base lorem ipsum - english">')
        self.assertContains(response, '<meta itemprop="description" content="base lorem ipsum - english">')
        self.assertContains(response, '<meta property="og:description" content="base lorem ipsum - english">')
        self.assertContains(response, '<meta property="og:title" content="page one">')
        self.assertContains(
            response, '<meta property="og:url" content="http://example.com%s">' % page1.get_absolute_url("en")
        )

        title_ext_en.description = "custom description"
        title_ext_en.save()
        with self.login_user_context(self.user):
            response = self.client.get(page_url_en)
        self.assertContains(response, '<meta name="description" content="custom description">')
        self.assertContains(response, '<meta name="twitter:description" content="custom description">')
        self.assertContains(response, '<meta itemprop="description" content="custom description">')

        # page1 = page1.get_draft_object()
        title_en = page1.get_title_obj(language="en", fallback=False)
        title_ext_en = title_en.titlemeta
        title_ext_en.twitter_description = "twitter custom description"
        title_ext_en.og_description = "og custom description"
        title_ext_en.save()
        # page1.publish("en")
        with self.login_user_context(self.user):
            response = self.client.get(page_url_en)
        self.assertContains(response, '<meta name="description" content="custom description">')
        self.assertContains(response, '<meta name="twitter:description" content="twitter custom description">')
        self.assertContains(response, '<meta property="og:description" content="og custom description">')

        title2_en = page2.get_title_obj(language="en", fallback=False)
        title2_en.meta_description = self.title_data["description"]
        title2_en.save()
        # English language
        # A page with no title meta, and yet the meta description is there
        page_url_en = page2.get_absolute_url('en')
        with self.login_user_context(self.user):
            response1 = self.client.get(page_url_en)
        self.assertContains(response1, '<meta name="description" content="base lorem ipsum - english">')
        self.assertContains(response1, '<meta name="twitter:description" content="base lorem ipsum - english">')
        self.assertContains(response1, '<meta itemprop="description" content="base lorem ipsum - english">')
        self.assertContains(response1, '<meta property="og:description" content="base lorem ipsum - english">')
        self.assertNotContains(response1, '<meta property="og:title" content="page one">')
        self.assertNotContains(
            response1, '<meta property="og:url" content="http://example.com%s">' % page1.get_absolute_url("en")
        )
