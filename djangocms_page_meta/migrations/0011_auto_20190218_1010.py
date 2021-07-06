# Generated by Django 2.1.7 on 2019-02-18 10:10

import django.db.models.deletion
import filer.fields.file
from django.conf import settings
from django.db import DatabaseError, migrations, models
from django.db.migrations.recorder import MigrationRecorder

# django cms 3 backwards compatibility for the Title model.
page_content_model = 'cms.Title'
try:
    if MigrationRecorder.Migration.objects.filter(app="cms", name="0032_remove_title_to_pagecontent").count():
        page_content_model = "cms.PageContent"
except DatabaseError as error:
    page_content_model = "cms.PageContent"


class Migration(migrations.Migration):

    dependencies = [
        ("djangocms_page_meta", "0010_auto_20180108_2316"),
    ]

    operations = [
        migrations.AlterField(
            model_name="genericmetaattribute",
            name="page",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="extra",
                to="djangocms_page_meta.PageMeta",
            ),
        ),
        migrations.AlterField(
            model_name="genericmetaattribute",
            name="title",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="extra",
                to="djangocms_page_meta.TitleMeta",
            ),
        ),
        migrations.AlterField(
            model_name="pagemeta",
            name="image",
            field=filer.fields.file.FilerFileField(
                blank=True,
                help_text="Used if title image is empty.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="djangocms_page_meta_page",
                to="filer.File",
            ),
        ),
        migrations.AlterField(
            model_name="pagemeta",
            name="og_author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Author account",
            ),
        ),
        migrations.AlterField(
            model_name="pagemeta",
            name="public_extension",
            field=models.OneToOneField(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="draft_extension",
                to="djangocms_page_meta.PageMeta",
            ),
        ),
        migrations.AlterField(
            model_name="titlemeta",
            name="extended_object",
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE,
                                       to=page_content_model),
        ),
        migrations.AlterField(
            model_name="titlemeta",
            name="image",
            field=filer.fields.file.FilerFileField(
                blank=True,
                help_text="If empty, page image will be used for all languages.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="djangocms_page_meta_title",
                to="filer.File",
            ),
        ),
        migrations.AlterField(
            model_name="titlemeta",
            name="public_extension",
            field=models.OneToOneField(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="draft_extension",
                to="djangocms_page_meta.TitleMeta",
            ),
        ),
    ]
