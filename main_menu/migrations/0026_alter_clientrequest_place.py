# Generated by Django 4.1.2 on 2022-12-10 23:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_menu', '0025_clientrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientrequest',
            name='place',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
