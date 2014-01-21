.. _installation:

============
Installation
============

#. Install djangocms-page-meta::

    $ pip install djangocms-page-meta

   or from the repository::

    $ pip install -e https://github.com/nephila/djangocms-page-meta#egg=djangocms-page-meta

#. Then add it to INSTALLED_APPS along with its dependencies::

    'filer',
    'meta',
    'djangocms_page_meta',

#. Synchronize the database with syncdb::

    $ python manage.py syncdb

   or migrate::

    $ python manage.py migrate

#. Configure `django-meta`_ adding at least ``META_SITE_DOMAIN`` and
   ``META_SITE_PROTOCOL`` to the project configuration. See `django-meta`_
   for further detail.

#. That's all!

************
Dependencies
************

* `django-filer`_ >= 0.9.5
* `django-meta`_  >= 0.1.0



.. _django-filer: https://pypi.python.org/pypi/django-filer
.. _django-meta: https://pypi.python.org/pypi/django-meta