# Generated by Django 2.2.6 on 2020-02-20 21:44

from django.db import migrations
import project.utils.slug


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0008_presenter_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presenter',
            name='slug',
            field=project.utils.slug.EnglishAutoSlugField(blank=True, editable=False, overwrite=True, populate_from=['name']),
        ),
    ]