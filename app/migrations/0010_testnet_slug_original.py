# Generated by Django 3.2.16 on 2023-01-21 01:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20230119_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='testnet',
            name='slug_original',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
    ]
