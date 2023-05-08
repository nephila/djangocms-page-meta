# Generated by Django 2.2 on 2020-08-21 14:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("djangocms_page_meta", "0012_auto_20200706_1230"),
    ]

    operations = [
        migrations.AddField(
            model_name="titlemeta",
            name="schemaorg_description",
            field=models.CharField(
                blank=True, help_text="Description of the item.", max_length=255, verbose_name="Schemaorg Description"
            ),
        ),
        migrations.AddField(
            model_name="titlemeta",
            name="schemaorg_name",
            field=models.CharField(
                blank=True, help_text="Name of the item.", max_length=255, verbose_name="Schemaorg Name"
            ),
        ),
        migrations.AlterField(
            model_name="pagemeta",
            name="schemaorg_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Article", "Article"),
                    ("Blog", "Blog"),
                    ("WebPage", "Page"),
                    ("WebSite", "WebSite"),
                    ("Event", "Event"),
                    ("Product", "Product"),
                    ("Place", "Place"),
                    ("Person", "Person"),
                    ("Book", "Book"),
                    ("LocalBusiness", "LocalBusiness"),
                    ("Organization", "Organization"),
                    ("Review", "Review"),
                ],
                help_text="Use Article for generic pages.",
                max_length=255,
                verbose_name="Resource type",
            ),
        ),
    ]
