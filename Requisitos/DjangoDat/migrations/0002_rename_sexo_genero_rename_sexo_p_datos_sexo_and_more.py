# Generated by Django 5.0.6 on 2024-08-26 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoDat', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sexo',
            new_name='Genero',
        ),
        migrations.RenameField(
            model_name='datos',
            old_name='Sexo_p',
            new_name='Sexo',
        ),
        migrations.RenameField(
            model_name='genero',
            old_name='Sexo_p',
            new_name='Sexo',
        ),
    ]
