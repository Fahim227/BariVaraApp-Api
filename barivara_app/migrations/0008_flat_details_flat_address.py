# Generated by Django 3.2.9 on 2021-12-01 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barivara_app', '0007_alter_flat_details_flat_renter_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat_details',
            name='flat_address',
            field=models.CharField(default='', max_length=200),
        ),
    ]