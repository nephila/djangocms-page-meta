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

.. _PAGE_META_TWITTER_DESCRIPTION_LENGTH:

PAGE_META_TWITTER_DESCRIPTION_LENGTH
------------------------------------

Set the max length of the Twitter card description field.
Default is ``280``.

.. _PAGE_META_ROBOTS_CHOICES:

PAGE_META_ROBOTS_CHOICES
------------------------

Set all the available choices for robots meta tag.
Default is:

.. code-block:: python

    (
        ("none", _("None [noindex, nofollow]")),
        ("noindex", _("No Index")),
        ("nofollow", _("No Follow")),
        ("noimageindex", _("No Image Index")),
        ("nosnippet", _("No Snippet")),
        ("noarchive", _("No Archive")),
        ("notranslate", _("No Translate")),
        ("nositelinkssearchbox", _("No Site Links Search Box")),
    )

django-meta configuration
=========================

djangocms-page-meta needs a working `django-meta`_ configuration,
especially the `template setup`_ section.

Please check `django-meta configuration`_ for complete settings details.


.. _template setup: https://django-meta.readthedocs.io/en/latest/models.html#reference-template
.. _django-meta configuration: https://django-meta.readthedocs.io/en/latest/settings.html
.. _django-meta: https://pypi.python.org/pypi/django-meta
