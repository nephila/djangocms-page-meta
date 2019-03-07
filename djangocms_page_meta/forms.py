# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django import forms
from django.core.validators import MaxLengthValidator

from .models import GenericMetaAttribute, TitleMeta
from .settings import get_setting


class TitleMetaAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.base_fields['description'].validators = [
            MaxLengthValidator(get_setting('DESCRIPTION_LENGTH'))
        ]
        self.base_fields['twitter_description'].validators = [
            MaxLengthValidator(get_setting('TWITTER_DESCRIPTION_LENGTH'))
        ]
        super(TitleMetaAdminForm, self).__init__(*args, **kwargs)

    class Meta:
        model = TitleMeta
        exclude = ()


class GenericAttributeInlineForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(GenericAttributeInlineForm, self).__init__(*args, **kwargs)
        self.fields['attribute'].widget.attrs[
            'placeholder'
        ] = GenericMetaAttribute.DEFAULT_ATTRIBUTE

    class Meta:
        model = GenericMetaAttribute
        exclude = ()
