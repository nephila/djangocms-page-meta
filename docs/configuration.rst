.. _meta-settings:

=============
Configuration
=============


Settings
========

.. _PAGE_META_DESCRIPTION_LENGTH:

PAGE_META_DESCRIPTION_LENGTH
----------------------------

Set the max length of the HTML meta description field.
Default is ``320``.

.. PAGE_META_TWITTER_DESCRIPTION_LENGTH:

PAGE_META_TWITTER_DESCRIPTION_LENGTH
------------------------------------

Set the max length of the Twitter card description field.
Default is ``280``.

.. PAGE_META_ROBOTS_CHOICES:

PAGE_META_ROBOTS_CHOICES
------------------------------------

Choose what directives can be displayed inside robots meta tags.
Default are ``none``, ``noindex``, ``noimageindex``, ``nofollow``, ``nosnippet``, ``noarchive``, and ``notranslate`` (`here`_'s a list of all the directives for robots meta tags).

This must be an iterable containing ``(('value', 'human readable name'),)`` tuples.


django-meta configuration
=========================

djangocms-page-meta needs a working `django-meta`_ configuration,
especially the `template setup`_ section.

Basic config:

In ``settings.py``:

.. code:: python

    META_SITE_PROTOCOL = 'http'  # OR 'https'
    META_USE_SITES = True  # OR META_SITE_DOMAIN='example.com'

In ``templates/base.html``:

.. code:: htmldjango

    {% load cms_tags menu_tags sekizai_tags page_meta_tags %}
    {% page_meta request.current_page as page_meta %}
    ...
    <head>
    ...
    {% include 'djangocms_page_meta/meta.html' with meta=page_meta %}
    </head>
    ...


Please check `django-meta configuration`_ for complete settings details.


.. _template setup: https://django-meta.readthedocs.io/en/latest/models.html#reference-template
.. _django-meta configuration: https://django-meta.readthedocs.io/en/latest/settings.html
.. _django-meta: https://pypi.python.org/pypi/django-meta
.. _here: https://developers.google.com/search/reference/robots_meta_tag#directives_1
