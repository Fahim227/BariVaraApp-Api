# Generated by Django 3.2.9 on 2021-11-30 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barivara_app', '0002_earning_flat_details_remain'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='referal_id',
            field=models.CharField(default='default1', max_length=200),
        ),
    ]
