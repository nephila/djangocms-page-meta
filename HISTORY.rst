.. :changelog:

*******
History
*******

0.10.0 (2019-12-27)
===================

* Move from djangocms-helper to django-app-helper
* Improve toolbar performance

0.9.0 (2019-08-22)
==================

* Add support for django CMS 3.7 / Django 2.2
* Remove support for Django < 1.11 / Python 3.4

0.8.5 (2019-03-22)
==================

* Fix error in migration missing on_delete argument

0.8.4 (2019-03-11)
==================

* Add Django 2.0 and Django 2.1 compatibility
* Add django CMS 3.6 compatibility
* Fixes a crash on creating new pagetype with djangocms 3.5.2

0.8.3 (2018-04-07)
==================

* Remove description when creating a CMS page
* Provide page dates meta if PageMeta does not exists
* Improve compatibility with Django 3.5

0.8.2 (2018-02-22)
==================

* Change method of patching PageAdmin for better compatibility with other addons

0.8.1 (2018-02-17)
==================

* Fix duplicate GenericMetaAttribute on publish
* Fix error on Divio cloud when description fields length is not set

0.8.0 (2018-01-14)
==================

* Add Django 1.11 support
* Add django CMS 3.5 support
* Drop django CMS 3.2, 3.3
* Add support for filer canonical URL
* Do not fail if request is not in context
* Make HTML and twitter description fields length configurable

0.7.0 (2016-12-04)
==================

* Drop Django 1.7 and below
* Drop django CMS 3.1 and below
* Add Django 1.10 support

0.6.3 (2016-10-22)
==================

* Added support for django CMS 3.4

0.6.2 (2016-08-01)
==================

* Conditionally show page description field if not empty

0.6.1 (2016-06-20)
==================

* Drop unique index on generic meta attributes

0.6 (2016-06-05)
================

* Let settings be used as defaults
* Added support for fb_pages attribute
* Added support for generic meta attributes

0.5.11 (2016-03-17)
===================

* Make object type not required

0.5.10 (2016-03-03)
===================

* Fix handling Google+ author URL

0.5.9 (2016-02-25)
==================

* Fix issue with Django 1.9

0.5.8 (2016-02-23)
==================

* Improve Aldryn support
* Catch AttributeError in get_page_meta

0.5.7 (2016-01-09)
==================

* Fix handling of pages in non existing languages
* Add support for Aldryn environment

0.5.6 (2015-10-03)
==================

* Fix error when retrieing tags from djangocms-page-tags
* Add support for django CMS 3.2
* Add support for Django 1.8

0.5.5 (2015-08-21)
==================

* Different approach at fix error when page is None
* Better fallback mechanism
* Update i18n

0.5.4 (2015-08-08)
==================

* Fix error when page is None
* Code cleanup
* Add pep8/isort to tests
* Add missing migration

0.5.3 (2015-06-29)
==================

* Fix Django 1.7 migration
* Update testing configuration

0.5.2 (2015-06-28)
==================

* Compatibility with django CMS 3.1.1

0.5.1 (2015-06-06)
==================

* Make south migrations indipendent from djangocms-helper

0.5 (2015-06-06)
================

* Add support for custom user model
* Fix the length of SEO fields
* Use djangocms-helper for tests
* Add support for Django 1.7
* Add support for django CMS 3.1

0.4.1 (2014-08-10)
==================

* Minor fixes

0.4.0 (2014-04-19)
==================

* django CMS 3 final release support
* Moved some code to external django-meta-mixin application

0.3.3 (2014-03-23)
==================

* Better support for sn-dependent descriptions

0.3.2 (2014-03-07)
==================

* Add different descriptions for each supported social network

0.3.1 (2014-02-13)
==================

* Fix permission name

0.3.0 (2014-02-02)
==================

* Fix for django CMS 3 develop update

0.2.1 (2014-01-26)
==================

* Vendorizing django-meta compatibility templatetags

0.2.0 (2014-01-22)
==================

* Put toolbar menu items in a submenu

0.1.0 (2014-01-21)
==================

* Experimental release.
