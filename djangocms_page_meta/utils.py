from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.translation import get_language_from_request
from meta import settings as meta_settings


def get_cache_key(page, language):
    """
    Create the cache key for the current page and language
    """
    from cms.cache import _get_cache_key

    try:
        site_id = page.node.site_id
    except AttributeError:  # CMS_3_4
        site_id = page.site_id
    return _get_cache_key("page_meta", page, language, site_id)


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

    try:
        meta_key = get_cache_key(page, language)
    except AttributeError:
        return None
    meta = cache.get(meta_key)
    if not meta:
        meta = Meta()
        title = page.get_title_obj(language)
        meta.extra_custom_props = []

        meta.title = page.get_page_title(language)
        if not meta.title:
            meta.title = page.get_title(language)

        if title.meta_description:
            meta.description = title.meta_description.strip()
        try:
            titlemeta = title.titlemeta
            if titlemeta.description:
                meta.description = titlemeta.description.strip()
            if titlemeta.keywords:
                meta.keywords = titlemeta.keywords.strip().split(",")
            meta.locale = titlemeta.locale
            meta.og_description = titlemeta.og_description.strip()
            if not meta.og_description:
                meta.og_description = meta.description
            meta.twitter_description = titlemeta.twitter_description.strip()
            if not meta.twitter_description:
                meta.twitter_description = meta.description
            if titlemeta.image:
                meta.image = title.titlemeta.image.canonical_url or title.titlemeta.image.url
                meta.schemaorg_image = meta.image
            meta.schemaorg_description = titlemeta.schemaorg_description.strip()
            if not meta.schemaorg_description:
                meta.schemaorg_description = meta.description
            meta.schemaorg_name = titlemeta.schemaorg_name
            if not meta.schemaorg_name:
                meta.schemaorg_name = meta.title
            for item in titlemeta.extra.all():
                attribute = item.attribute
                if not attribute:
                    attribute = item.DEFAULT_ATTRIBUTE
                meta.extra_custom_props.append((attribute, item.name, item.value))
        except (TitleMeta.DoesNotExist, AttributeError):
            # Skipping title-level metas
            if meta.description:
                meta.og_description = meta.description
                meta.schemaorg_description = meta.description
                meta.twitter_description = meta.description
        defaults = {
            "object_type": meta_settings.FB_TYPE,
            "og_type": meta_settings.FB_TYPE,
            "og_app_id": meta_settings.FB_APPID,
            "fb_pages": meta_settings.FB_PAGES,
            "og_profile_id": meta_settings.FB_PROFILE_ID,
            "og_publisher": meta_settings.FB_PUBLISHER,
            "og_author_url": meta_settings.FB_AUTHOR_URL,
            "twitter_type": meta_settings.TWITTER_TYPE,
            "twitter_site": meta_settings.TWITTER_SITE,
            "twitter_author": meta_settings.TWITTER_AUTHOR,
            "schemaorg_type": meta_settings.SCHEMAORG_TYPE,
            "schemaorg_datePublished": page.publication_date.isoformat() if page.publication_date else None,
            "schemaorg_dateModified": page.changed_date.isoformat() if page.changed_date else None,
        }
        try:
            pagemeta = page.pagemeta
            meta.object_type = pagemeta.og_type
            meta.og_type = pagemeta.og_type
            meta.og_app_id = pagemeta.og_app_id
            meta.fb_pages = pagemeta.fb_pages
            meta.og_profile_id = pagemeta.og_author_fbid
            meta.twitter_type = pagemeta.twitter_type
            meta.twitter_site = pagemeta.twitter_site
            meta.twitter_author = pagemeta.twitter_author
            meta.schemaorg_type = pagemeta.schemaorg_type
            if page.publication_date:
                meta.published_time = page.publication_date.isoformat()
            if page.changed_date:
                meta.modified_time = page.changed_date.isoformat()
            if page.publication_end_date:
                meta.expiration_time = page.publication_end_date.isoformat()
            if meta.og_type == "article":
                meta.og_publisher = pagemeta.og_publisher
                meta.og_author_url = pagemeta.og_author_url
                try:
                    from djangocms_page_tags.utils import get_page_tags, get_title_tags

                    tags = list(get_title_tags(page, language))
                    tags += list(get_page_tags(page))
                    meta.tag = ",".join([tag.name for tag in tags])
                except ImportError:
                    # djangocms-page-tags not available
                    pass
            if not meta.image and pagemeta.image:
                meta.image = pagemeta.image.canonical_url or pagemeta.image.url
            for item in pagemeta.extra.all():
                attribute = item.attribute
                if not attribute:
                    attribute = item.DEFAULT_ATTRIBUTE
                meta.extra_custom_props.append((attribute, item.name, item.value))
        except PageMeta.DoesNotExist:
            pass
        for attr, val in defaults.items():
            if not getattr(meta, attr, "") and val:
                setattr(meta, attr, val)
        meta.url = page.get_absolute_url(language)
        meta.schemaorg_url = meta.url
        cache.set(meta_key, meta)
    return meta


def get_metatags(request):
    language = get_language_from_request(request, check_path=True)
    meta = get_page_meta(request.current_page, language)
    return mark_safe(
        render_to_string(request=request, template_name="djangocms_page_meta/meta.html", context={"meta": meta})
    )
