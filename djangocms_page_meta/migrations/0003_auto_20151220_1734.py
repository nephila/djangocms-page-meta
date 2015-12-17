# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_page_meta', '0002_auto_20150807_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagemeta',
            name='gplus_author',
            field=models.CharField(default='', help_text='Use the Google+ Name (together with ) or the complete path to the page.', max_length=255, verbose_name='Author Google+ URL', blank=True),
        ),
        migrations.AlterField(
            model_name='pagemeta',
            name='twitter_author',
            field=models.CharField(default='', help_text="'@' character not required.", max_length=255, verbose_name='Author Twitter Account', blank=True),
        ),
        migrations.AlterField(
            model_name='pagemeta',
            name='twitter_site',
            field=models.CharField(default='', help_text="'@' characther not required.", max_length=255, verbose_name='Website Twitter Account', blank=True),
        ),
    ]
