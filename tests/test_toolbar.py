from cms.toolbar.items import Menu, ModalItem, SubMenu
from cms.utils.i18n import get_language_object
from django.contrib.auth.models import Permission, User
from django.test.utils import override_settings
from django.urls import reverse
from django.utils.encoding import force_str

from djangocms_page_meta.cms_toolbars import PAGE_META_ITEM_TITLE, PAGE_META_MENU_TITLE
from djangocms_page_meta.models import PageMeta, TitleMeta

from . import BaseTest


class ToolbarTest(BaseTest):
    def test_no_page(self):
        """
        Test that no page menu is present if request not in a page
        """
        from cms.toolbar.toolbar import CMSToolbar

        request = self.get_page_request(None, self.user, "/", edit=True)
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        page_menu = toolbar.find_items(Menu, name="Page")
        self.assertEqual(page_menu, [])

    def test_no_perm(self):
        """
        Test that no page menu is present if user has no perm
        """
        from cms.toolbar.toolbar import CMSToolbar

        page1, __ = self.get_pages()
        request = self.get_page_request(page1, self.user_staff, "/", edit=True)
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        page_menu = toolbar.find_items(Menu, name="Page")
        try:
            self.assertEqual(page_menu, [])
        except AssertionError:
            meta_menu = page_menu[0].item.find_items(SubMenu, name=force_str(PAGE_META_MENU_TITLE))
            self.assertEqual(meta_menu, [])

    def test_page_types(self):
        """
        Test that page meta menu is not displayed on page types.
        """
        from cms.toolbar.toolbar import CMSToolbar

        page1, __ = self.get_pages()
        page1.is_page_type = True
        page1.save()
        self.user_staff.user_permissions.add(Permission.objects.get(codename="change_page"))
        self.user_staff = User.objects.get(pk=self.user_staff.pk)
        request = self.get_page_request(page1, self.user_staff, "/", edit=True)
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        page_menu = toolbar.menus["page"]
        page_items = page_menu.find_items(SubMenu, name=force_str(PAGE_META_MENU_TITLE))
        self.assertEqual(len(page_items), 0)

    def test_perm(self):
        """
        Test that page meta menu is present if user has Page.change_perm
        """
        from cms.toolbar.toolbar import CMSToolbar

        page1, __ = self.get_pages()
        self.user_staff.user_permissions.add(Permission.objects.get(codename="change_page"))
        self.user_staff = User.objects.get(pk=self.user_staff.pk)
        request = self.get_page_request(page1, self.user_staff, "/", edit=True)
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        page_menu = toolbar.menus["page"]
        meta_menu = page_menu.find_items(SubMenu, name=force_str(PAGE_META_MENU_TITLE))[0].item
        self.assertEqual(len(meta_menu.find_items(ModalItem, name="{}...".format(force_str(PAGE_META_ITEM_TITLE)))), 1)

    @override_settings(CMS_PERMISSION=True)
    def test_perm_permissions(self):
        """
        Test that no page menu is present if user has general page Page.change_perm  but not permission on current page
        """
        from cms.toolbar.toolbar import CMSToolbar

        page1, __ = self.get_pages()
        self.user_staff.user_permissions.add(Permission.objects.get(codename="change_page"))
        self.user_staff = User.objects.get(pk=self.user_staff.pk)
        request = self.get_page_request(page1, self.user_staff, "/", edit=True)
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        page_menu = toolbar.find_items(Menu, name="Page")
        try:
            self.assertEqual(page_menu, [])
        except AssertionError:
            meta_menu = page_menu[0].item.find_items(SubMenu, name=force_str(PAGE_META_MENU_TITLE))
            self.assertEqual(meta_menu, [])

    def test_toolbar(self):
        """
        Test that PageMeta/TitleMeta items are present for superuser
        """
        from cms.toolbar.toolbar import CMSToolbar

        NEW_CMS_LANGS = {  # noqa: N806
            1: [
                {
                    "code": "en",
                    "name": "English",
                    "public": True,
                },
                {
                    "code": "it",
                    "name": "Italiano",
                    "public": True,
                },
            ],
            "default": {
                "hide_untranslated": False,
            },
        }

        page1, __ = self.get_pages()
        with self.settings(CMS_LANGUAGES=NEW_CMS_LANGS):
            request = self.get_page_request(page1, self.user, "/", edit=True)
            toolbar = CMSToolbar(request)
            toolbar.get_left_items()
            page_menu = toolbar.menus["page"]
            meta_menu = page_menu.find_items(SubMenu, name=force_str(PAGE_META_MENU_TITLE))[0].item
            self.assertEqual(
                len(meta_menu.find_items(ModalItem, name="{}...".format(force_str(PAGE_META_ITEM_TITLE)))), 1
            )
            self.assertEqual(len(meta_menu.find_items(ModalItem)), len(NEW_CMS_LANGS[1]) + 1)

    def test_toolbar_with_items(self):
        """
        Test that PageMeta/TitleMeta items are present for superuser if PageMeta/TitleMeta exists for current page
        """
        from cms.toolbar.toolbar import CMSToolbar

        page1, __ = self.get_pages()
        page_ext = PageMeta.objects.create(extended_object=page1)
        title_meta = TitleMeta.objects.create(extended_object=page1.get_title_obj("en"))
        request = self.get_page_request(page1, self.user, "/", edit=True)
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        page_menu = toolbar.menus["page"]
        meta_menu = page_menu.find_items(SubMenu, name=force_str(PAGE_META_MENU_TITLE))[0].item
        pagemeta_menu = meta_menu.find_items(ModalItem, name="{}...".format(force_str(PAGE_META_ITEM_TITLE)))
        self.assertEqual(len(pagemeta_menu), 1)
        self.assertTrue(
            pagemeta_menu[0].item.url.startswith(
                reverse("admin:djangocms_page_meta_pagemeta_change", args=(page_ext.pk,))
            )
        )
        url_change = False
        url_add = False
        for title in page1.title_set.all():
            language = get_language_object(title.language)
            titlemeta_menu = meta_menu.find_items(ModalItem, name="{}...".format(language["name"]))
            self.assertEqual(len(titlemeta_menu), 1)
            try:
                title_ext = TitleMeta.objects.get(extended_object_id=title.pk)
                self.assertEqual(title_ext, title_meta)
                self.assertTrue(
                    titlemeta_menu[0].item.url.startswith(
                        reverse("admin:djangocms_page_meta_titlemeta_change", args=(title_ext.pk,))
                    )
                )
                url_change = True
            except TitleMeta.DoesNotExist:
                self.assertTrue(
                    titlemeta_menu[0].item.url.startswith(reverse("admin:djangocms_page_meta_titlemeta_add"))
                )
                url_add = True
        self.assertTrue(url_change and url_add)
