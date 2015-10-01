# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django import forms

from .models import TitleMeta


class TitleMetaAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TitleMetaAdminForm, self).__init__(*args, **kwargs)
        self.fields['description'].max_length = 160

    class Meta:
        model = TitleMeta
        exclude = ()
