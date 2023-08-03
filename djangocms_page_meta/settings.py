from django.utils.translation import gettext_lazy as _


def get_setting(name):
    from django.conf import settings

    description_length = getattr(settings, "PAGE_META_DESCRIPTION_LENGTH", None) or 320

    tw_description_length = getattr(settings, "PAGE_META_TWITTER_DESCRIPTION_LENGTH", None) or 320

    robots_choices = getattr(settings, "PAGE_META_ROBOTS_CHOICES", None) or (
        ("none", _("None [noindex, nofollow]")),
        ("noindex", _("No Index")),
        ("nofollow", _("No Follow")),
        ("noimageindex", _("No Image Index")),
        ("nosnippet", _("No Snippet")),
        ("noarchive", _("No Archive")),
        ("notranslate", _("No Translate")),
        ("nositelinkssearchbox", _("No Site Links Search Box")),
    )

    default = {
        "PAGE_META_DESCRIPTION_LENGTH": description_length,
        "PAGE_META_TWITTER_DESCRIPTION_LENGTH": tw_description_length,
        "PAGE_META_ROBOTS_CHOICES": robots_choices,
    }
    return default["PAGE_META_%s" % name]
