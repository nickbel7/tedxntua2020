# Generated by Django 2.2.6 on 2020-02-26 19:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_remove_notification_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='start',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]