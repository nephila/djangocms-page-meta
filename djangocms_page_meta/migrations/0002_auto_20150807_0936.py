from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("djangocms_page_meta", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pagemeta",
            name="og_author_fbid",
            field=models.CharField(
                default=b"",
                help_text="Use Facebook numeric ID.",
                max_length=16,
                verbose_name="Author Facebook ID",
                blank=True,
            ),
        ),
    ]
