# Generated by Django 3.0.6 on 2020-05-25 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparser', '0006_auto_20200525_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='published_date',
            field=models.DateTimeField(verbose_name='Дата публикации'),
        ),
    ]
