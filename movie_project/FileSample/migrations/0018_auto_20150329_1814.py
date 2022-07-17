# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0017_auto_20150328_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('propietario', models.CharField(max_length=128, verbose_name='Propietario', db_column='Propietario')),
                ('titulo', models.CharField(max_length=255, verbose_name='Titulo', db_column='Titulo')),
                ('autor', models.CharField(max_length=128, verbose_name='Autor', db_column='Autor')),
                ('nivel_autoria', models.CharField(max_length=20, verbose_name='Nivel de Autoria', db_column='Nivel_Autoria')),
                ('anno', models.IntegerField(max_length=10, verbose_name='Año', db_column='Anno')),
                ('pais', models.CharField(max_length=30, verbose_name='Pais', db_column='Pais')),
                ('ciudad', models.CharField(max_length=30, verbose_name='Ciudad', db_column='Ciudad')),
                ('editorial', models.CharField(max_length=50, verbose_name='Editorial', db_column='Editorial')),
                ('publicacion', models.CharField(max_length=100, verbose_name='Publicacion', db_column='Publicacion')),
                ('numero', models.CharField(max_length=10, verbose_name='Numero', db_column='Numero')),
                ('volumen', models.IntegerField(max_length=10, verbose_name='Volumen', db_column='Volumen')),
                ('nivel_mes', models.IntegerField(max_length=5, verbose_name='Nivel_MES', db_column='Nivel_MES')),
                ('aprobacion', models.BooleanField(max_length=1000, verbose_name='Aprobacion', db_column='Aprobacion')),
                ('fichero', models.CharField(max_length=255, verbose_name='Asociar fichero', db_column='Direccion_Fichero_Asociado')),
            ],
            options={
                'verbose_name': 'Publicacion',
                'verbose_name_plural': 'Publicaciones',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='continent',
            options={'verbose_name': 'Continente', 'verbose_name_plural': 'Continentes'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Pais', 'verbose_name_plural': 'Paises'},
        ),
        migrations.AlterModelOptions(
            name='file',
            options={'verbose_name': 'File', 'verbose_name_plural': 'Files'},
        ),
    ]
