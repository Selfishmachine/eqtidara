# Generated by Django 3.2.8 on 2021-12-16 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0007_unit_unit_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='phone',
            field=models.CharField(default=22, max_length=12, verbose_name='phone'),
            preserve_default=False,
        ),
    ]
