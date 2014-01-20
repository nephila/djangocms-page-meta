.. _meta-usage:

#####
Usage
#####

********************************************
Assigning meta information to pages / titles
********************************************

Meta information can be assigned from the admin interface or the toolbar.

In the toolbar you will find a ``Page meta-information`` submenu in the
``Page`` menu, with two or more sub-items:

* Common: it allows to edit page-wide (language independent) meta information
* One entry per active language to edit language dependent information


**************************
Rendering meta information
**************************

To render provided meta information you must add these lines in the main
template:

.. code-block:: html+django

    {% load page_meta_tags %}
    {% page_meta request.current_page as meta %}

    <html>
         <head>
         {% include 'djangocms_page_meta/meta.html' with meta=meta %}
         </head>
    </html>


page_meta
=========

``page_meta`` templatetags extract information from the given page to a context
variable that can be passed to the included template for rendering.

**Arguments:**

* ``page``: a page instance (tipically current page);
* ``varname``: the name of the context variable to save data to.