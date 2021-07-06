import warnings
from app_helper.base_test import BaseTestCase
from django.core.cache import cache
from django.test import RequestFactory, TestCase, TransactionTestCase

from collections import OrderedDict
from copy import deepcopy

class DummyTokens(list):
    def __init__(self, *tokens):
        super().__init__(["dummy_tag"] + list(tokens))

    def split_contents(self):
        return self


class BaseTest(BaseTestCase):
    """
    Base class with utility function
    """

    page_data = {}
    _pages_data = (
        {
            "en": {"title": "page one", "template": "page_meta.html", "publish": True},
            "fr-fr": {"title": "page un", "publish": True},
            "it": {"title": "pagina uno", "publish": True},
        },
        {
            "en": {"title": "page two", "template": "page_meta.html", "publish": True},
            "fr-fr": {"title": "page deux", "publish": True},
            "it": {"title": "pagina due", "publish": True},
        },
    )
    title_data = {
        "keywords": "keyword1, keyword2, keyword3",
        "description": "base lorem ipsum - english",
        "og_description": "opengraph - lorem ipsum - english",
        "twitter_description": "twitter - lorem ipsum - english",
        "schemaorg_description": "gplus - lorem ipsum - english",
    }
    title_data_it = {
        "keywords": "parola1, parola2, parola3",
        "description": "base lorem ipsum - italian",
        "og_description": "opengraph - lorem ipsum - italian",
        "twitter_description": "twitter - lorem ipsum - italian",
        "schemaorg_description": "gplus - lorem ipsum - italian",
    }
    og_data = {
        "og_type": "article",
        "og_author_url": "https://facebook.com/FakeUser",
        "og_author_fbid": "123456789",
        "og_publisher": "https://facebook.com/FakeUser",
        "og_app_id": "123456789",
        "fb_pages": "PAGES123456789",
    }
    twitter_data = {
        "twitter_author": "fake_user",
        "twitter_site": "fake_site",
        "twitter_type": "summary",
    }

    def get_pages(self):
        """
        Create pages using self._pages_data and self.languages
        :return: list of created pages
        """
        return self.create_pages(self._pages_data, self.languages)

    @staticmethod
    def create_pages(source, languages):
        """
        Build pages according to the pages data provided by :py:meth:`get_pages_data`
        and returns the list of the draft version of each
        """
        from cms.api import create_page, create_title

        pages = OrderedDict()
        has_apphook = False
        home_set = False
        for page_data in source:
            main_data = deepcopy(page_data[languages[0]])
            if "publish" in main_data:
                main_data["published"] = main_data.pop("publish")
            main_data["language"] = languages[0]
            if main_data.get("parent", None):
                main_data["parent"] = pages[main_data["parent"]]
            page = create_page(**main_data)
            has_apphook = has_apphook or "apphook" in main_data
            for lang in languages[1:]:
                if lang in page_data:
                    publish = False
                    title_data = deepcopy(page_data[lang])
                    if "publish" in title_data:
                        publish = title_data.pop("publish")
                    if "published" in title_data:
                        publish = title_data.pop("published")
                    title_data["language"] = lang
                    title_data["page"] = page
                    create_title(**title_data)
            if not home_set and hasattr(page, "set_as_homepage") and main_data.get("published", False):
                page.set_as_homepage()
                home_set = True
            pages[page.get_slug(languages[0])] = page
        if has_apphook:
            reload_urls(settings, cms_apps=True)
        return list(pages.values())

    def get_page_request(self, page, user, path=None, edit=False, lang="en", use_middlewares=False, secure=False):
        """Deprecated, use :py:meth:`get_toolbar_request`."""
        warnings.warn(
            "get_page_request has been renamed tp `get_toolbar_request` and it will be removed in version 3.0",
            PendingDeprecationWarning,
        )
        return self.get_toolbar_request(page, user, path, edit, lang, use_middlewares, secure)

    def get_toolbar_request(self, page, user, path=None, edit=False, lang="en", use_middlewares=False, secure=False):
        """
        Create a GET request for the given page suitable for use the django CMS toolbar.

        This method requires django CMS installed to work. It will raise an ImportError otherwise; not a big deal
        as this method makes sense only in a django CMS environment.

        :param page: current page object
        :param user: current user
        :param path: path (if different from the current page path)
        :param edit: whether enabling editing mode
        :param lang: request language
        :param use_middlewares: pass the request through configured middlewares.
        :param secure: create HTTPS request
        :return: request
        """
        from cms.utils.conf import get_cms_setting

        path = path or page and page.get_absolute_url(lang)

        request = RequestFactory().get(path, secure=secure)
        return self._prepare_request(request, page, user, lang, use_middlewares, use_toolbar=True, secure=secure)

    def setUp(self):
        super().setUp()
        cache.clear()
