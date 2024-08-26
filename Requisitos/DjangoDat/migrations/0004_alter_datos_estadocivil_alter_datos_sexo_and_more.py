# Generated by Django 5.0.6 on 2024-08-26 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoDat', '0003_alter_lugar_nacimiento_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos',
            name='EstadoCivil',
            field=models.CharField(choices=[('Casado', 'Casado'), ('Soltero', 'Soltero')], max_length=50, verbose_name='Estado civil'),
        ),
        migrations.AlterField(
            model_name='datos',
            name='Sexo',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=50, verbose_name='Genero'),
        ),
        migrations.DeleteModel(
            name='Estado_Civil',
        ),
        migrations.DeleteModel(
            name='Genero',
        ),
    ]
