===================
djangocms-page-meta
===================

.. image:: https://badge.fury.io/py/djangocms-page-meta.png
    :target: http://badge.fury.io/py/djangocms-page-meta
    
.. image:: https://travis-ci.org/nephila/djangocms-page-meta.png?branch=master
        :target: https://travis-ci.org/nephila/djangocms-page-meta

.. image:: https://pypip.in/d/djangocms-page-meta/badge.png
        :target: https://crate.io/packages/djangocms-page-meta?version=latest

.. image:: https://coveralls.io/repos/nephila/djangocms-page-meta/badge.png?branch=master
        :target: https://coveralls.io/r/nephila/djangocms-page-meta?branch=master


Tagged pages for django CMS 3


Quickstart
----------

Install djangocms-page-meta::

    pip install djangocms-page-meta

Then add it to INSTALLED_APPS along with its dependencies::

    'meta',

Execute migration or syncdb::

    $ python manage.py syncdb

or::

    $ python manage.py migrate


Usage
-----

You will find two new items in the toolbar Page menu:

* Title tags (per language)
* Page tags (global)

These items allows to add tags to ``Title`` and ``Page`` instances, respectively

Templatetags
------------

``djangocms-page-meta`` allows showing tags using four templatetags

* ``include_page_meta``
* ``include_title_tags``
* ``page_meta``
* ``title_tags``


.. image:: https://d2weczhvl823v0.cloudfront.net/nephila/djangocms-page-meta/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

