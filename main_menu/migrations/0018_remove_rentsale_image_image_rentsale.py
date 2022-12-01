# Generated by Django 4.1.2 on 2022-12-01 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_menu', '0017_alter_rentsale_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentsale',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='rentsale',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main_menu.rentsale'),
            preserve_default=False,
        ),
    ]
