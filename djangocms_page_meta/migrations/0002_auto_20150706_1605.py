# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_page_meta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericMetaTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('content', models.CharField(max_length=128)),
                ('page', models.ForeignKey(related_name='tags', blank=True, to='djangocms_page_meta.PageMeta')),
            ],
            options={
                'verbose_name': 'Meta tag',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='pagemeta',
            name='gplus_type',
            field=models.CharField(choices=[(b'Article', 'Article'), (b'Blog', 'Blog'), (b'Book', 'Book'), (b'Event', 'Event'), (b'LocalBusiness', 'LocalBusiness'), (b'Organization', 'Organization'), (b'Person', 'Person'), (b'Product', 'Product'), (b'Review', 'Review')], max_length=255, blank=True, help_text='Use Article for generic pages.', null=True, verbose_name='Resource type'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pagemeta',
            name='og_type',
            field=models.CharField(choices=[(b'article', 'Article'), (b'website', 'Website')], max_length=255, blank=True, help_text='Use Article for generic pages.', null=True, verbose_name='Resource type'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pagemeta',
            name='twitter_type',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Resource type', choices=[(b'summary', 'Summary'), (b'summary_large_image', 'Summary large image'), (b'product', 'Product'), (b'photo', 'Photo'), (b'player', 'Player'), (b'app', 'App')]),
            preserve_default=True,
        ),
    ]
