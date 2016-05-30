# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django import forms

from .models import GenericMetaAttribute, TitleMeta


class TitleMetaAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TitleMetaAdminForm, self).__init__(*args, **kwargs)
        self.fields['description'].max_length = 160

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
