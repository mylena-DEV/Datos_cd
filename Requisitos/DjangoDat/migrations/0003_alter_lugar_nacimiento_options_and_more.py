# Generated by Django 5.0.6 on 2024-08-26 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoDat', '0002_rename_sexo_genero_rename_sexo_p_datos_sexo_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lugar_nacimiento',
            options={'verbose_name': 'Nombre de la Ciudad', 'verbose_name_plural': 'Nombre de la Ciudad'},
        ),
        migrations.RenameField(
            model_name='lugar_nacimiento',
            old_name='Nombre_Lugar',
            new_name='Ciudad_de_nacimiento',
        ),
    ]
