# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_page_meta', '0005_pagemeta_fb_pages'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericMetaAttribute',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('attribute', models.CharField(blank=True, help_text='Custom attribute', max_length=200, default='', verbose_name='attribute')),
                ('name', models.CharField(help_text='Meta attribute name', max_length=200, verbose_name='name')),
                ('value', models.CharField(help_text='Meta attribute value', max_length=2000, verbose_name='value')),
            ],
            options={
                'verbose_name_plural': 'Page meta info (language-dependent)',
                'verbose_name': 'Page meta info (language-dependent)',
            },
        ),
        migrations.AlterModelOptions(
            name='pagemeta',
            options={'verbose_name_plural': 'Page meta info (all languages)', 'verbose_name': 'Page meta info (all languages)'},
        ),
        migrations.AlterModelOptions(
            name='titlemeta',
            options={'verbose_name_plural': 'Page meta info (language-dependent)', 'verbose_name': 'Page meta info (language-dependent)'},
        ),
        migrations.AddField(
            model_name='genericmetaattribute',
            name='page',
            field=models.ForeignKey(related_name='extra', blank=True, null=True, to='djangocms_page_meta.PageMeta', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='genericmetaattribute',
            name='title',
            field=models.ForeignKey(related_name='extra', blank=True, null=True, to='djangocms_page_meta.TitleMeta', on_delete=models.CASCADE),
        ),
    ]
