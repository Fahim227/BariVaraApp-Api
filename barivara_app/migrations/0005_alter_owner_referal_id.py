# Generated by Django 3.2.9 on 2021-11-30 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barivara_app', '0004_remove_renter_rented_flat_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='referal_id',
            field=models.CharField(default='default', max_length=200),
        ),
    ]
