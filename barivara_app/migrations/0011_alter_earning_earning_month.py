# Generated by Django 3.2.9 on 2021-12-02 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barivara_app', '0010_alter_earning_earning_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='earning',
            name='earning_month',
            field=models.CharField(null=True, max_length=10),
        ),
    ]
