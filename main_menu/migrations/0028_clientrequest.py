# Generated by Django 4.1.2 on 2022-12-14 05:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_menu', '0027_delete_clientrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, validators=[django.core.validators.MinValueValidator(3)])),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
