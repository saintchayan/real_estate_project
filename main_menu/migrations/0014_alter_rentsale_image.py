# Generated by Django 4.1.2 on 2022-11-28 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_menu', '0013_alter_rentsale_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentsale',
            name='image',
            field=models.ImageField(blank=True, height_field=500, null=True, upload_to='images/', width_field=700),
        ),
    ]
