from cms.models import Page
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.test.client import RequestFactory

from djangocms_page_meta.admin import DefaultMetaImageAdmin
from djangocms_page_meta.models import DefaultMetaImage

from . import BaseTest

page_admin = admin.site._registry[Page]


class AdminPageTest(BaseTest):
    def test_get_form_no_obj(self):
        """
        Test that the returned form has not been modified by the meta patch
        when no page object is specified
        """
        request = self.get_page_request(None, self.user, "/", edit=True)
        form = page_admin.get_form(request)
        self.assertEqual(form.base_fields.get("meta_description"), None)

    def test_get_form_with_obj(self):
        """
        Test that the returned form has been modified by the meta patch
        """
        page1, _page2 = self.get_pages()

        request = self.get_page_request(page1, self.user, "/", edit=True)
        form = page_admin.get_form(request, page1)
        self.assertEqual(form.base_fields.get("meta_description"), None)

    def test_get_form_with_obj_description(self):
        """
        Test that the returned form has been modified by the meta patch
        """
        page1, _page2 = self.get_pages()
        title = page1.get_title_obj("en")
        title.meta_description = "something"
        title.save()

        request = self.get_page_request(page1, self.user, "/", edit=True)
        form = page_admin.get_form(request, page1)
        self.assertNotEqual(form.base_fields.get("meta_description"), None)

    def test_default_meta_image_admin_permissions(self):
        admin = DefaultMetaImageAdmin(DefaultMetaImage, AdminSite())
        request = RequestFactory()
        request.user = self.user
        self.assertFalse(admin.has_add_permission(request))
        self.assertFalse(admin.has_delete_permission(request))
