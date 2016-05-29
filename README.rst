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

Support Python version:

* Python 2.6
* Python 2.7
* Python 3.3
* Python 3.4
* Python 3.5

Supported Django versions:

* Django 1.6
* Django 1.7
* Django 1.8
* Django 1.9

Supported django CMS versions:

* django CMS 3.x

.. warning:: Version 0.6 will be the last one supporting Python 2.6, Python 3.3,
             Django<1.8 and django CMS<3.2.


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
        'djangocms_page_meta',

#. Synchronize the database with syncdb::

        $ python manage.py syncdb

   or migrate::

        $ python manage.py migrate

#. Configuration:

   There is no special configuration for djangocms-page-meta, but make sure you set the necessary configuration for `django-meta`_.

#. That's all!

Dependencies
============

* `django-filer`_ >= 0.9.5
* `django-meta`_  >= 1.0

.. _django-filer: https://pypi.python.org/pypi/django-filer
.. _django-meta: https://pypi.python.org/pypi/django-meta

*************
Documentation
*************

For package documentation see http://djangocms-page-meta.readthedocs.org/.

