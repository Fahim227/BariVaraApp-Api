# Generated by Django 3.1.7 on 2021-12-17 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barivara_app', '0017_auto_20211213_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat_details',
            name='is_rented',
            field=models.BooleanField(default=False),
        ),
    ]
