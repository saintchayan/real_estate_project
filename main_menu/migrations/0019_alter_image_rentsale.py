# Generated by Django 4.1.2 on 2022-12-01 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_menu', '0018_remove_rentsale_image_image_rentsale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='rentsale',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_menu.rentsale'),
        ),
    ]
