===================
djangocms-page-meta
===================

|Gitter| |PyPiVersion| |PyVersion| |GAStatus| |TestCoverage| |CodeClimate| |License|

Meta tag information for django CMS 3 pages

Python: 3.6, 3.7, 3.8

Django: 2.2, 3.0, 3.1

django CMS: 3.7, 3.8


**********
Quickstart
**********

#. A working django CMS environment is required for djangocms-page-meta to work. Refer to `django CMS documentation`_ for how to install and configure django CMS.

#. Install djangocms-page-meta::

        $ pip install djangocms-page-meta

   or from the repository::

        pip install -e git+https://github.com/nephila/djangocms-page-meta#egg=djangocms-page-meta

#. Then add it to INSTALLED_APPS along with its dependencies::

        'filer',
        'meta',
        'easy_thumbnails',
        'djangocms_page_meta',

#. Synchronize the database with syncdb::

        $ python manage.py syncdb

   or migrate::

        $ python manage.py migrate

#. Configuration:

   See `usage`_ and `configuration`_ section in the documentation.

#. That's all!

.. note:: Enabling this will **hide** django CMS own **Meta description** field to keep all the meta
          information in the same part of the interface. If the django CMS field is set, it will still
          be shown (and used by djangocms-page-meta).

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


.. |Gitter| image:: https://img.shields.io/badge/GITTER-join%20chat-brightgreen.svg?style=flat-square
    :target: https://gitter.im/nephila/applications
    :alt: Join the Gitter chat

.. |PyPiVersion| image:: https://img.shields.io/pypi/v/djangocms-redirect.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-redirect
    :alt: Latest PyPI version

.. |PyVersion| image:: https://img.shields.io/pypi/pyversions/djangocms-redirect.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-redirect
    :alt: Python versions

.. |GAStatus| image:: https://github.com/nephila/djangocms-redirect/workflows/Tox%20tests/badge.svg
    :target: https://github.com/nephila/djangocms-redirect
    :alt: Latest CI build status

.. |TestCoverage| image:: https://img.shields.io/coveralls/nephila/djangocms-redirect/master.svg?style=flat-square
    :target: https://coveralls.io/r/nephila/djangocms-redirect?branch=master
    :alt: Test coverage

.. |License| image:: https://img.shields.io/github/license/nephila/djangocms-redirect.svg?style=flat-square
   :target: https://pypi.python.org/pypi/djangocms-redirect/
    :alt: License

.. |CodeClimate| image:: https://codeclimate.com/github/nephila/djangocms-redirect/badges/gpa.svg?style=flat-square
   :target: https://codeclimate.com/github/nephila/djangocms-redirect
   :alt: Code Climate
