# Generated by Django 4.1.2 on 2022-11-08 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_menu', '0003_alter_rentsale_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rentsale',
            old_name='price_in_lirs',
            new_name='price_in_lira',
        ),
    ]
