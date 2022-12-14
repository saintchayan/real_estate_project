# Generated by Django 4.1.2 on 2022-12-10 23:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_menu', '0024_rentsale_floor_rentsale_room_rentsale_square'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(3)])),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('place', models.CharField(max_length=20)),
            ],
        ),
    ]
