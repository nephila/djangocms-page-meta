# -*- coding: utf-8 -*-
from django import forms
from parler.forms import TranslatableModelForm

from .models import TitleMeta


class TitleMetaAdminForm(TranslatableModelForm):

    def __init__(self, *args, **kwargs):
        super(TitleMetaAdminForm, self).__init__(*args, **kwargs)
        self.fields['description'].max_length = 160

    class Meta:
        model = TitleMeta
        exclude = ()