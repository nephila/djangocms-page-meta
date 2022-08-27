===================
djangocms-page-meta
===================

|Gitter| |PyPiVersion| |PyVersion| |GAStatus| |TestCoverage| |CodeClimate| |License|

Meta tag information for django CMS 3 pages

Python: 3.7, 3.8, 3.9, 3.10

Django: 2.2, 3.2

django CMS: 3.7 - 3.10


**********
Quickstart
**********

#. A working django CMS environment is required for djangocms-page-meta to work. Refer to `django CMS documentation`_ for how to install and configure django CMS.

#. Install djangocms-page-meta::

        $ pip install djangocms-page-meta

   or from the repository::

        pip install -e git+https://github.com/nephila/djangocms-page-meta#egg=djangocms-page-meta

#. Then add it to INSTALLED_APPS along with its dependencies::

        "filer",
        "meta",
        "easy_thumbnails",
        "djangocms_page_meta",

#. Migrate the database::

        $ python manage.py migrate

#. Configuration:

   See `usage`_ and `configuration`_ section in the documentation.

#. That's all!

.. note:: Enabling this will **hide** django CMS own **Meta description** field to keep all the meta
          information in the same part of the interface. If the django CMS field is set, it will still
          be shown (and used by djangocms-page-meta).

**************************
django-app-enabler support
**************************

`django-app-enabler`_ is supported.

You can either

* Installation & configuration: ``python -mapp_enabler install djangocms-page-meta``
* Autoconfiguration: ``python -mapp_enabler enable djangocms_page_meta``

Fully using this package will require some template changes that cannot be modified by ``django-app-enabler``:

* Load template tag in the page like outlined in `usage`_ page;
* Run migrations: ``python manage.py migrate``

Check `usage`_ documentation for details.

Dependencies
============

* `django-filer`_
* `django-meta`_

*************
Documentation
*************

For package documentation see https://djangocms-page-meta.readthedocs.io/.


.. _django-filer: https://pypi.python.org/pypi/django-filer
.. _django-meta: https://pypi.python.org/pypi/django-meta
.. _configuration: https://djangocms-page-meta.readthedocs.io/en/latest/configuration.html
.. _usage: https://djangocms-page-meta.readthedocs.io/en/latest/usage.html
.. _django CMS documentation: https://django-cms.readthedocs.io/en/latest
.. _django-app-enabler: https://github.com/nephila/django-app-enabler


.. |Gitter| image:: https://img.shields.io/badge/GITTER-join%20chat-brightgreen.svg?style=flat-square
    :target: https://gitter.im/nephila/applications
    :alt: Join the Gitter chat

.. |PyPiVersion| image:: https://img.shields.io/pypi/v/djangocms-page-meta.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-page-meta
    :alt: Latest PyPI version

.. |PyVersion| image:: https://img.shields.io/pypi/pyversions/djangocms-page-meta.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-page-meta
    :alt: Python versions

.. |GAStatus| image:: https://github.com/nephila/djangocms-redirect/workflows/Tox%20tests/badge.svg
    :target: https://github.com/nephila/djangocms-page-meta
    :alt: Latest CI build status

.. |TestCoverage| image:: https://img.shields.io/coveralls/nephila/djangocms-page-meta/master.svg?style=flat-square
    :target: https://coveralls.io/r/nephila/djangocms-page-meta?branch=master
    :alt: Test coverage

.. |License| image:: https://img.shields.io/github/license/nephila/djangocms-page-meta.svg?style=flat-square
   :target: https://pypi.python.org/pypi/djangocms-page-meta/
    :alt: License

.. |CodeClimate| image:: https://codeclimate.com/github/nephila/djangocms-page-meta/badges/gpa.svg?style=flat-square
   :target: https://codeclimate.com/github/nephila/djangocms-page-meta
   :alt: Code Climate
