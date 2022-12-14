# Generated by Django 4.1.2 on 2022-12-09 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_menu', '0023_remove_rentsale_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentsale',
            name='floor',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rentsale',
            name='room',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rentsale',
            name='square',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
