# Generated by Django 3.2.9 on 2021-12-07 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barivara_app', '0014_alter_remain_remain_month'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='renter',
            name='owner_referal_id',
        ),
    ]
