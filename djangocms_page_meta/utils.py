# -*- coding: utf-8 -*-


def get_cache_key(page, language):
    """
    Create the cache key for the current page and language
    """
    try:
        from cms.cache import _get_cache_key
    except ImportError:
        from cms.templatetags.cms_tags import _get_cache_key
    site_id = page.site_id
    return _get_cache_key('page_meta', page, language, site_id)


def get_page_meta(page, language):
    """
    Retrieves all the meta information for the page in the given language

    :param page: a Page instance
    :param lang: a language code

    :return: Meta instance
    :type: object
    """
    from django.core.cache import cache
    from meta.views import Meta
    from .models import PageMeta, TitleMeta

    meta_key = get_cache_key(page, language)
    meta = cache.get(meta_key)
    if not meta:
        meta = Meta()
        title = page.get_title_obj(language)

        meta.title = page.get_page_title(language)
        if not meta.title:
            meta.title = page.get_title(language)

        try:
            titlemeta = title.titlemeta
            meta.description = titlemeta.description.strip()
            if titlemeta.keywords:
                meta.keywords = titlemeta.keywords.strip().split(",")
            meta.locale = titlemeta.locale
            meta.og_description = titlemeta.og_description.strip()
            meta.twitter_description = titlemeta.twitter_description.strip()
            meta.gplus_description = titlemeta.gplus_description.strip()
            if titlemeta.image:
                meta.image = title.titlemeta.image.url
        except TitleMeta.DoesNotExist:
            # Skipping title-level metas
            pass
        try:
            pagemeta = page.pagemeta
            meta.object_type = pagemeta.og_type
            meta.og_type = pagemeta.og_type
            meta.og_app_id = pagemeta.og_app_id
            meta.og_profile_id = pagemeta.og_author_fbid
            meta.twitter_type = pagemeta.twitter_type
            meta.twitter_site = pagemeta.twitter_site
            meta.twitter_author = pagemeta.twitter_author
            meta.gplus_type = pagemeta.gplus_type
            meta.gplus_author = pagemeta.gplus_author
            meta.published_time = page.publication_date.isoformat()
            meta.modified_time = page.changed_date.isoformat()
            meta.tags = pagemeta.tags.all()
            if page.publication_end_date:
                meta.expiration_time = page.publication_end_date.isoformat()
            if meta.og_type == 'article':
                meta.og_publisher = pagemeta.og_publisher
                if pagemeta.og_author_url:
                    meta.og_author_url = pagemeta.og_author_url
                try:
                    from djangocms_page_meta.utils import get_title_tags, get_page_meta
                    tags = get_title_tags(page, language)
                    tags += get_page_meta(page, language)
                    meta.tag = ",".join(tags)
                except ImportError:
                    # djangocms-page-meta not available
                    pass
            if not meta.image and pagemeta.image:
                meta.image = pagemeta.image.url
        except PageMeta.DoesNotExist:
            # Skipping page-level metas
            pass
        if not meta.description and page.get_meta_description(language):
            meta.description = page.get_meta_description(language).strip()
        meta.url = page.get_absolute_url(language)
    return meta
