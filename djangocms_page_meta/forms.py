from django import forms
from django.core.validators import MaxLengthValidator

from .models import GenericMetaAttribute, PageMeta, TitleMeta
from .settings import get_setting


class PageMetaAdminForm(forms.ModelForm):
    robots = forms.MultipleChoiceField(
        choices=get_setting("ROBOTS_CHOICES"),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs.get("instance"):
            self.initial["robots"] = kwargs.get("instance").robots_list

    class Meta:
        model = PageMeta
        exclude = ()


class TitleMetaAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.base_fields["description"].validators = [MaxLengthValidator(get_setting("DESCRIPTION_LENGTH"))]
        self.base_fields["twitter_description"].validators = [
            MaxLengthValidator(get_setting("TWITTER_DESCRIPTION_LENGTH"))
        ]
        super().__init__(*args, **kwargs)

    class Meta:
        model = TitleMeta
        exclude = ()


class GenericAttributeInlineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["attribute"].widget.attrs["placeholder"] = GenericMetaAttribute.DEFAULT_ATTRIBUTE

    class Meta:
        model = GenericMetaAttribute
        exclude = ()
