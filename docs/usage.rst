.. _meta-usage:

=====
Usage
=====

********************************************
Assigning meta information to pages / titles
********************************************

Meta information can be assigned from the admin interface or the toolbar.

In the toolbar you will find a ``Meta-information`` submenu in the
``Page`` menu, with three or more sub-items:

* Default meta image: it allows to add a default meta image, that will be used in all pages if no specific page image is set.
* Common: it allows to edit page-wide (language independent) meta information;
* One entry per active language to edit language dependent information.


**************************
Rendering meta information
**************************

To render provided meta information you must add these lines in the main
template:

.. code-block:: html+django

    {% load page_meta_tags %}
    {% page_meta request.current_page as page_meta %}

    [...]
    <!-- This must be in the head -->
    {% include 'djangocms_page_meta/meta.html' with meta=page_meta %}

When using microdata from [Schema.org](https://schema.org/docs/gs.html#microdata_how), you must add the type attribute to the body or html tag:

.. code-block:: html+django

    {% autoescape off %}
    <html {% schemaorg_html_scope page_meta.schemaorg_type %}>
    {% endautoescape %}

or:

.. code-block:: html+django

    {% autoescape off %}
    <body {% schemaorg_html_scope page_meta.schemaorg_type %}>
    {% endautoescape %}

Don't forget to load ``meta`` in your template!

.. code-block:: html+django

    {% load cms_tags menu_tags sekizai_tags page_meta_tags meta %}

********************
Supported attributes
********************

``djangocms-page-meta`` currently offers partial support for `OpenGraph`_,
`Twitter Cards`_, `Schema.org microdata`_ and robots meta tag. As a generic
application ``djangocms-page-meta`` cannot cover every use case while
still being useful to most people.


Generic HTML
============

* description: HTML meta description of the page
* keywords: HTML meta keywords


.. note:: Enabling this will **hide** django CMS own **Meta description** field to keep all the meta
          information in the same part of the interface. If the django CMS field is set, it will still
          be shown (and used by djangocms-page-meta).


OpenGraph
=========

The following properties are supported:

* og:title
* og:url
* og:description
* og:image
* og:type
* og:site_name
* og:locale
* article:author:url
* article:author:first_name
* article:author:last_name
* article:published_time
* article:modified_time
* article:expiration_time
* article:publisher
* article:tag
* fb:app_id
* fb:profile_id
* fb:pages

See `Facebook OpenGraph documentation`_ for more information
about each property.


Twitter Cards
=============

The following properties are supported:

* twitter:domain
* twitter:card
* twitter:title
* twitter:url
* twitter:description
* twitter:image
* twitter:creator
* twitter:site_name

See `Twitter documentation`_ for more information
about each property.


Schema.org microdata
====================

Support for `Schema.org microdata`_ is very basic, and limited to
the ``<html>`` & ``<body>`` tags. You might need to further
customize the markup according to you specific content.

As of now support is limited to the the following data:

* rel=author, via ``link rel="author"`` in the ``<head>``
* name
* image
* datePublished
* dateModified
* url
* description
* image
* type (i.e. itemscope), appended to ``<html>`` or ``<body>`` tag

Currently all the accepted values for **type** are provided as valid
choices; not all of them are actually sensible values for CMS pages
and ``djangocms-page-meta`` offers limited support for the attributes
required by some accepted types.

``Article`` or ``Blog`` type should be sensible for most use cases.

************
Generic meta
************

If different metas are needed, a generic model exists that allows to add
custom metas.

Both ``PageMeta`` and ``TitleMeta`` provides an inline model that allows to
define custom metas; model provides three fields:

* attribute: meta attribute
* name: name of the meta
* value: value of the meta

Each inline will be rendered as::

    <meta {{ attribute }}="{{ name }}" content="{{ value }}" />


************
Templatetags
************

page_meta
=========

``page_meta`` templatetags extract information from the given page to a context
variable that can be passed to the included template for rendering.

**Arguments:**

* ``page``: a page instance (tipically current page);
* ``varname``: the name of the context variable to save data to.

.. _OpenGraph: http://ogp.me/
.. _Facebook OpenGraph documentation: https://developers.facebook.com/docs/reference/opengraph/object-type/article/
.. _Twitter documentation: https://dev.twitter.com/docs/cards
.. _Schema.org microdata: http://schema.org/docs/gs.html
.. _Twitter Cards: https://dev.twitter.com/cards
