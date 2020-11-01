try:
    from divio_cli import forms
except ImportError:
    from aldryn_client import forms

OBJECT_TYPES = (
    ("", "----"),
    ("Article", "Article"),
    ("Website", "Website"),
)

PROTOCOLS = (
    ("http", "http"),
    ("https", "https"),
)


class Form(forms.BaseForm):
    META_SITE_PROTOCOL = forms.SelectField(
        "Site protocol",
        choices=PROTOCOLS,
    )
    META_SITE_TYPE = forms.SelectField("Site type", choices=OBJECT_TYPES, required=False)
    META_SITE_NAME = forms.CharField("Site name", required=False)
    META_USE_OG_PROPERTIES = forms.CheckboxField("Render the OpenGraph properties", required=False)
    META_USE_TWITTER_PROPERTIES = forms.CheckboxField("Render the Twitter properties", required=False)
    PAGE_META_DESCRIPTION_LENGTH = forms.CharField("Max description field length (default: 320)", required=False)
    PAGE_META_TWITTER_DESCRIPTION_LENGTH = forms.CharField(
        "Max twitter description field length (default: 280)", required=False
    )
    META_USE_SCHEMAORG_PROPERTIES = forms.CheckboxField("Render the Schema.org properties", required=False)

    def to_settings(self, data, settings):
        settings["META_SITE_PROTOCOL"] = data["META_SITE_PROTOCOL"]
        settings["META_SITE_TYPE"] = data["META_SITE_TYPE"]
        settings["META_SITE_NAME"] = data["META_SITE_NAME"]
        settings["META_INCLUDE_KEYWORDS"] = []
        settings["META_DEFAULT_KEYWORDS"] = []
        settings["META_USE_OG_PROPERTIES"] = data["META_USE_OG_PROPERTIES"]
        settings["META_USE_TWITTER_PROPERTIES"] = data["META_USE_TWITTER_PROPERTIES"]
        settings["PAGE_META_TWITTER_DESCRIPTION_LENGTH"] = data["PAGE_META_TWITTER_DESCRIPTION_LENGTH"]
        settings["PAGE_META_DESCRIPTION_LENGTH"] = data["PAGE_META_DESCRIPTION_LENGTH"]
        settings["META_USE_TITLE_TAG"] = False
        settings["META_USE_SITES"] = True
        settings["META_USE_SCHEMAORG_PROPERTIES"] = data["META_USE_SCHEMAORG_PROPERTIES"]
        return settings
