# Generated by Django 3.2.9 on 2021-12-02 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barivara_app', '0013_alter_earning_earning_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remain',
            name='remain_month',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
