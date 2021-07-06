from cms.api import create_page
from cms.test_utils.testcases import CMSTestCase
from cms.toolbar.items import Menu, ModalItem, SubMenu
from cms.utils.i18n import get_language_object
from django.contrib.auth.models import Permission, User
from django.test.utils import override_settings
from django.urls import reverse
from django.utils.encoding import force_text

from djangocms_page_meta.cms_toolbars import PAGE_META_ITEM_TITLE, PAGE_META_MENU_TITLE
from djangocms_page_meta.models import PageMeta, TitleMeta


class ToolbarTest(CMSTestCase):
    def test_no_page(self):
        """
        Test that no page menu is present if request not in a page
        """
        from cms.toolbar.toolbar import CMSToolbar

        superuser = self.get_superuser()
        request = self.get_page_request(None, superuser, "/")
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        page_menu = toolbar.find_items(Menu, name="Page")
        self.assertEqual(page_menu, [])

    @override_settings(CMS_PERMISSION=True)
    def test_perm_permissions(self):
        """
        Test that no page menu is present if user has general page Page.change_perm  but not permission on current page
        """
        from cms.toolbar.toolbar import CMSToolbar

        language = "en"
        page1 = create_page(title='test', template="page_meta.html", language=language)
        staff_no_permission = self._create_user("staff", is_staff=True, is_superuser=False)
        staff_no_permission.user_permissions.add(Permission.objects.get(codename="change_page"))
        staff_no_permission = User.objects.get(pk=staff_no_permission.pk)

        request = self.get_page_request(page1, staff_no_permission, "/")
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        page_menu = toolbar.find_items(Menu, name="Page")
        try:
            self.assertEqual(page_menu, [])
        except AssertionError:
            meta_menu = page_menu[0].item.find_items(SubMenu, name=force_text(PAGE_META_MENU_TITLE))
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

        language = "en"
        page1 = create_page(title='test', template="page_meta.html", language=language)
        with self.settings(CMS_LANGUAGES=NEW_CMS_LANGS):
            request = self.get_page_request(page1, self.get_superuser(), "/")
            toolbar = CMSToolbar(request)
            toolbar.edit_mode_active = True
            toolbar.get_left_items()
            page_menu = toolbar.menus["page"]
            meta_menu = page_menu.find_items(SubMenu, name=force_text(PAGE_META_MENU_TITLE))[0].item
            self.assertEqual(
                len(meta_menu.find_items(ModalItem, name="{}...".format(force_text(PAGE_META_ITEM_TITLE)))), 1
            )
            self.assertEqual(len(meta_menu.find_items(ModalItem)), len(NEW_CMS_LANGS[1]))

    def test_no_perm(self):
        """
        Test that no page menu is present if user has no perm
        """
        from cms.toolbar.toolbar import CMSToolbar

        language = "en"
        staff_no_permission = self._create_user("staff", is_staff=True, is_superuser=False)
        page1 = create_page(title="test", template="page_meta.html", language=language)
        request = self.get_page_request(page1, staff_no_permission, "/")
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        page_menu = toolbar.find_items(Menu, name="Page")
        try:
            self.assertEqual(page_menu, [])
        except AssertionError:
            meta_menu = page_menu[0].item.find_items(SubMenu, name=force_text(PAGE_META_MENU_TITLE))
            self.assertEqual(meta_menu, [])

    def test_perm(self):
        """
        Test that page meta menu is present if user has Page.change_perm
        """
        from cms.toolbar.toolbar import CMSToolbar

        language = "en"
        staff_no_permission = self._create_user("staff", is_staff=True, is_superuser=False)
        page1 = create_page(title="test", template="page_meta.html", language=language)

        staff_no_permission.user_permissions.add(Permission.objects.get(codename="change_page"))
        staff_no_permission = User.objects.get(pk=staff_no_permission.pk)
        request = self.get_page_request(page1, staff_no_permission, "/")

        toolbar = CMSToolbar(request)
        toolbar.edit_mode_active = True

        toolbar.get_left_items()
        page_menu = toolbar.menus["page"]
        meta_menu = page_menu.find_items(SubMenu, name=force_text(PAGE_META_MENU_TITLE))
        self.assertEqual(
            len(meta_menu[0].item.find_items(ModalItem, name="{}...".format(force_text(PAGE_META_ITEM_TITLE)))), 1
        )

    @override_settings(CMS_PERMISSION=True)
    def test_perm_permissions(self):
        """
        Test that no page menu is present if user has general page Page.change_perm but not permission on current page
        """
        from cms.toolbar.toolbar import CMSToolbar

        language = "en"
        page1 = create_page(title="test", template="page_meta.html", language=language)
        staff_no_permission = self._create_user("staff", is_staff=True, is_superuser=False)
        staff_no_permission.user_permissions.add(Permission.objects.get(codename="change_page"))
        staff_no_permission = User.objects.get(pk=staff_no_permission.pk)
        request = self.get_page_request(page1, staff_no_permission, "/")
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        page_menu = toolbar.find_items(Menu, name="Page")
        try:
            self.assertEqual(page_menu, [])
        except AssertionError:
            meta_menu = page_menu[0].item.find_items(SubMenu, name=force_text(PAGE_META_MENU_TITLE))
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

        language = "en"
        page1 = create_page(title="test", template="page_meta.html", language=language)
        with self.settings(CMS_LANGUAGES=NEW_CMS_LANGS):
            request = self.get_page_request(page1, self.get_superuser(), "/")
            toolbar = CMSToolbar(request)
            toolbar.edit_mode_active = True
            toolbar.get_left_items()
            page_menu = toolbar.menus["page"]
            meta_menu = page_menu.find_items(SubMenu, name=force_text(PAGE_META_MENU_TITLE))[0].item
            self.assertEqual(
                len(meta_menu.find_items(ModalItem, name="{}...".format(force_text(PAGE_META_ITEM_TITLE)))), 1
            )
            self.assertEqual(len(meta_menu.find_items(ModalItem)), len(NEW_CMS_LANGS[1]))

    def test_toolbar_with_items(self):
        """
        Test that PageMeta/TitleMeta items are present for superuser if PageMeta/TitleMeta exists for current page
        """
        from cms.toolbar.toolbar import CMSToolbar

        language = "en"
        page1 = create_page(title="test", template="page_meta.html", language=language)
        page_ext = PageMeta.objects.create(extended_object=page1)
        title_meta = TitleMeta.objects.create(extended_object=page1.get_title_obj("en"))
        request = self.get_page_request(page1, self.get_superuser(), "/")
        toolbar = CMSToolbar(request)
        toolbar.edit_mode_active = True
        toolbar.get_left_items()
        page_menu = toolbar.menus["page"]
        meta_menu = page_menu.find_items(SubMenu, name=force_text(PAGE_META_MENU_TITLE))[0].item
        pagemeta_menu = meta_menu.find_items(ModalItem, name="{}...".format(force_text(PAGE_META_ITEM_TITLE)))
        self.assertEqual(len(pagemeta_menu), 1)
        self.assertTrue(
            pagemeta_menu[0].item.url.startswith(
                reverse("admin:djangocms_page_meta_pagemeta_change", args=(page_ext.pk,))
            )
        )
        url_change = False
        for title in page1.pagecontent_set.all():
            language = get_language_object(title.language)
            titlemeta_menu = meta_menu.find_items(ModalItem, name="{}...".format(language["name"]))
            self.assertEqual(len(titlemeta_menu), 1)
            title_ext = TitleMeta.objects.get(extended_object_id=title.pk)
            self.assertEqual(title_ext, title_meta)
            self.assertTrue(
                titlemeta_menu[0].item.url.startswith(
                    reverse("admin:djangocms_page_meta_titlemeta_change", args=(title_ext.pk,))
                )
            )
            url_change = True

        self.assertTrue(url_change)
