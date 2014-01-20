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

In the toolbar you will find a ``Page meta-information`` submenu in the
``Page`` menu, with two or more sub-items.

See :ref:`meta-usage` for more information.

.. image:: https://d2weczhvl823v0.cloudfront.net/nephila/djangocms-page-meta/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

