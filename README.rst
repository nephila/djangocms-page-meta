===================
djangocms-page-meta
===================

.. image:: https://badge.fury.io/py/djangocms-page-meta.png
    :target: http://badge.fury.io/py/djangocms-page-meta
    
.. image:: https://travis-ci.org/nephila/djangocms-page-meta.png?branch=master
        :target: https://travis-ci.org/nephila/djangocms-page-meta

.. image:: https://pypip.in/d/djangocms-page-meta/badge.png
        :target: https://pypi.python.org/pypi/djangocms-page-meta

.. image:: https://coveralls.io/repos/nephila/djangocms-page-meta/badge.png?branch=master
        :target: https://coveralls.io/r/nephila/djangocms-page-meta?branch=master


Tagged pages for django CMS 3


Quickstart
----------

#. Install djangocms-page-meta::

        $ pip install djangocms-page-meta

   or from the repository::

        pip install -e https://github.com/nephila/djangocms-page-meta#egg=djangocms-page-meta

#. Then add it to INSTALLED_APPS along with its dependencies::

        'filer',
        'meta',
        'djangocms_page_meta',

#. Synchronize the database with syncdb::

        $ python manage.py syncdb

   or migrate::

        $ python manage.py migrate

#. That's all!

************
Dependencies
************

* `django-filer`_ >= 0.9.5
* `django-meta`_  >= 0.1.0

.. _django-filer: https://pypi.python.org/pypi/django-filer
.. _django-meta: https://pypi.python.org/pypi/django-meta

********
Python 3
********

`djangocms-page-meta` per-se is full Python 3.3 compatible; django-filer
python 3 compatible version is likely to be released soon (python 3 support
has been merged in develop).

Documentation
-------------

For package documentation see http://djangocms-page-meta.readthedocs.org/.


.. image:: https://d2weczhvl823v0.cloudfront.net/nephila/djangocms-page-meta/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

