from app_helper.base_test import BaseTestCase
from django.core.cache import cache


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

    def setUp(self):
        super().setUp()
        cache.clear()
