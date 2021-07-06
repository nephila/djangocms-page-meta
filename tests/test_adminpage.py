from cms.api import create_page
from cms.models import Page
from cms.test_utils.testcases import CMSTestCase
from django.contrib import admin

page_admin = admin.site._registry[Page]


class AdminPageTest(CMSTestCase):
    def test_get_form_no_obj(self):
        """
        Test that the returned form has not been modified by the meta patch
        when no page object is specified
        """
        request = self.get_page_request(None, self.user, "/")
        form = page_admin.get_form(request)
        self.assertEqual(form.base_fields.get("meta_description"), None)

    def test_get_form_with_obj(self):
        """
        Test that the returned form has been modified by the meta patch
        """
        language = "en"
        superuser = self.get_superuser()
        page1 = create_page(title="test", template="page_meta.html", language=language)

        request = self.get_page_request(page1, self.user, "/")
        form = page_admin.get_form(request, page1)
        self.assertEqual(form.base_fields.get("meta_description"), None)

    def test_get_form_with_obj_description(self):
        """
        Test that the returned form has been modified by the meta patch
        """
        from cms.toolbar.toolbar import CMSToolbar

        language = "en"
        page1 = create_page(title="test", template="page_meta.html", language=language)
        title = page1.get_title_obj(language="en", fallback=False)
        title.meta_description = "something"
        title.save()

        request = self.get_page_request(page1, self.user, "/")
        form = page_admin.get_form(request, page1)
        self.assertNotEqual(form.base_fields.get("meta_description"), None)
