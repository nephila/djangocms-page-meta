===================
djangocms-page-meta
===================

.. image:: https://img.shields.io/pypi/v/djangocms-page-meta.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-page-meta
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/djangocms-page-meta.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-page-meta
    :alt: Monthly downloads

.. image:: https://img.shields.io/pypi/pyversions/djangocms-page-meta.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-page-meta
    :alt: Python versions

.. image:: https://img.shields.io/travis/nephila/djangocms-page-meta.svg?style=flat-square
    :target: https://travis-ci.org/nephila/djangocms-page-meta
    :alt: Latest Travis CI build status

.. image:: https://img.shields.io/coveralls/nephila/djangocms-page-meta/master.svg?style=flat-square
    :target: https://coveralls.io/r/nephila/djangocms-page-meta?branch=master
    :alt: Test coverage

.. image:: https://img.shields.io/codecov/c/github/nephila/djangocms-page-meta/develop.svg?style=flat-square
    :target: https://codecov.io/github/nephila/djangocms-page-meta
    :alt: Test coverage

.. image:: https://codeclimate.com/github/nephila/djangocms-page-meta/badges/gpa.svg?style=flat-square
   :target: https://codeclimate.com/github/nephila/djangocms-page-meta
   :alt: Code Climate

Meta tag information for django CMS 3 pages

Python: 2.7, 3.4, 3.5

Django: 1.8 to 1.10

django CMS: 3.2 to 3.4

.. warning:: Since version 0.7, the support for Python 2.6, Python 3.3, Django<1.8 and django CMS<3.2
             has been dropped


**********
Quickstart
**********

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

   There is no special configuration for djangocms-page-meta, but make sure you set the necessary configuration for `django-meta`_, especially the `template setup`_ section

#. That's all!

Dependencies
============

* `django-filer`_ >= 1.2
* `django-meta`_  >= 1.3

.. _django-filer: https://pypi.python.org/pypi/django-filer
.. _django-meta: https://pypi.python.org/pypi/django-meta
.. _template setup: https://django-meta.readthedocs.io/en/latest/models.html#reference-template

*************
Documentation
*************

For package documentation see https://djangocms-page-meta.readthedocs.io/.



.. image:: https://d2weczhvl823v0.cloudfront.net/nephila/djangocms-page-meta/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

