# Generated by Django 3.2.8 on 2021-12-11 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0005_auto_20211211_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='location',
            field=models.TextField(blank=True, null=True, verbose_name='location'),
        ),
    ]
