# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.models import Page
from django.contrib import admin
from django.forms import fields

from . import BaseTest

page_admin = admin.site._registry[Page]


class AdminPageTest(BaseTest):

    def test_get_form_no_obj(self):
        """
        Test that the returned form has not been modified by the meta patch
        when no page object is specified
        """
        request = self.get_page_request(None, self.user, '/', edit=True)
        form = page_admin.get_form(request)
        self.assertIsInstance(
            form.base_fields.get('meta_description'),
            fields.CharField
        )

    def test_get_form_with_obj(self):
        """
        Test that the returned form has been modified by the meta patch
        """
        page1, _page2 = self.get_pages()

        request = self.get_page_request(page1, self.user, '/', edit=True)
        form = page_admin.get_form(request, page1)
        self.assertEqual(form.base_fields.get('meta_description'), None)
