from cms.models import Page
from django.contrib import admin

from cms.api import create_page
from cms.test_utils.testcases import CMSTestCase

from . import BaseTest

page_admin = admin.site._registry[Page]


class AdminPageTest(CMSTestCase):
    def test_get_form_no_obj(self):
        """
        Test that the returned form has not been modified by the meta patch
        when no page object is specified
        """
        request = self.get_page_request(None, self.get_superuser(), "/")
        form = page_admin.get_form(request)
        self.assertEqual(form.base_fields.get("meta_description"), None)

    def test_get_form_with_obj(self):
        """
        Test that the returned form has been modified by the meta patch
        """
        language = "en"
        superuser = self.get_superuser()
        page1 = create_page(title='test', template="page_meta.html", language=language)

        request = self.get_page_request(page1, superuser, "/")
        form = page_admin.get_form(request, page1)
        self.assertEqual(form.base_fields.get("meta_description"), None)

    def test_get_form_with_obj_description(self):
        """
        Test that the returned form has been modified by the meta patch
        """
        from cms.toolbar.toolbar import CMSToolbar

        # page1, _page2 = self.get_pages()
        language = "en"
        page1 = create_page(title='test', template="page_meta.html", language=language)
        title = page1.get_title_obj("en")
        title.meta_description = "something"
        title.save()

        request = self.get_page_request(page1, self.get_superuser(), "/")
        toolbar = CMSToolbar(request)
        toolbar.edit_mode_active = True
        form = page_admin.get_form(request, page1)
        test = form.base_fields.get("meta_description")
        self.assertNotEqual(form.base_fields.get("meta_description"), None)
