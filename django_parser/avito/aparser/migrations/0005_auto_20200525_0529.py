# Generated by Django 3.0.6 on 2020-05-25 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparser', '0004_auto_20200525_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.URLField(verbose_name='Ссылка на объявление'),
        ),
    ]
