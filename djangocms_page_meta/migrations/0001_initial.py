# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.file
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms', '0003_auto_20140926_2347'),
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageMeta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('og_type', models.CharField(help_text='Use Article for generic pages.', max_length=255, verbose_name='Resource type', choices=[(b'article', 'Article'), (b'website', 'Website')])),
                ('og_author_url', models.CharField(default=b'', max_length=255, verbose_name='Author Facebook URL', blank=True)),
                ('og_author_fbid', models.CharField(default=b'', help_text='Use Facebook numeric ID', max_length=16, verbose_name='Author Facebook ID', blank=True)),
                ('og_publisher', models.CharField(default=b'', max_length=255, verbose_name='Website Facebook URL', blank=True)),
                ('og_app_id', models.CharField(default=b'', max_length=255, verbose_name='Facebook App ID', blank=True)),
                ('twitter_author', models.CharField(default=b'', help_text='"@" sign not required.', max_length=255, verbose_name='Author Twitter Account', blank=True)),
                ('twitter_site', models.CharField(default=b'', help_text='"@" sign not required.', max_length=255, verbose_name='Website Twitter Account', blank=True)),
                ('twitter_type', models.CharField(max_length=255, verbose_name='Resource type', choices=[(b'summary', 'Summary'), (b'summary_large_image', 'Summary large image'), (b'product', 'Product'), (b'photo', 'Photo'), (b'player', 'Player'), (b'app', 'App')])),
                ('gplus_author', models.CharField(default=b'', help_text='Use the Google+ Name (together with "+") or the complete path to the page.', max_length=255, verbose_name='Author Google+ URL', blank=True)),
                ('gplus_type', models.CharField(help_text='Use Article for generic pages.', max_length=255, verbose_name='Resource type', choices=[(b'Article', 'Article'), (b'Blog', 'Blog'), (b'Book', 'Book'), (b'Event', 'Event'), (b'LocalBusiness', 'LocalBusiness'), (b'Organization', 'Organization'), (b'Person', 'Person'), (b'Product', 'Product'), (b'Review', 'Review')])),
                ('extended_object', models.OneToOneField(editable=False, to='cms.Page')),
                ('image', filer.fields.file.FilerFileField(related_name='djangocms_page_meta_page', blank=True, to='filer.File', help_text='Used if title image is empty.', null=True)),
                ('og_author', models.ForeignKey(verbose_name='Author account', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('public_extension', models.OneToOneField(related_name='draft_extension', null=True, editable=False, to='djangocms_page_meta.PageMeta')),
            ],
            options={
                'verbose_name': 'Page meta info (all languages)',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TitleMeta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.CharField(default=b'', max_length=400, blank=True)),
                ('description', models.CharField(default=b'', max_length=400, blank=True)),
                ('og_description', models.CharField(default=b'', max_length=400, verbose_name='Facebook Description', blank=True)),
                ('twitter_description', models.CharField(default=b'', max_length=140, verbose_name='Twitter Description', blank=True)),
                ('gplus_description', models.CharField(default=b'', max_length=400, verbose_name='Google+ Description', blank=True)),
                ('extended_object', models.OneToOneField(editable=False, to='cms.Title')),
                ('image', filer.fields.file.FilerFileField(related_name='djangocms_page_meta_title', blank=True, to='filer.File', help_text='If empty, page image will be used for all languages.', null=True)),
                ('public_extension', models.OneToOneField(related_name='draft_extension', null=True, editable=False, to='djangocms_page_meta.TitleMeta')),
            ],
            options={
                'verbose_name': 'Page meta info (language-dependent)',
            },
            bases=(models.Model,),
        ),
    ]
