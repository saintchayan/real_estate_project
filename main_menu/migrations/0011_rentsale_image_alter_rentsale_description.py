# Generated by Django 4.1.2 on 2022-11-27 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_menu', '0010_alter_rentsale_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentsale',
            name='image',
            field=models.ImageField(blank=True, height_field=500, max_length=10, null=True, upload_to='images/', width_field=700),
        ),
        migrations.AlterField(
            model_name='rentsale',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
