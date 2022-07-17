# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0025_patente'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultadoIntroducido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('propietario', models.CharField(max_length=128, verbose_name='Propietario:', db_column='Propietario')),
                ('nombre_obra', models.CharField(max_length=255, verbose_name='Nombre de la obra:', db_column='Nombre_Obra')),
                ('ciencia_obra', models.CharField(max_length=100, verbose_name='Ciencia de la obra:', db_column='Ciencia_Obra')),
                ('fecha', models.DateField()),
                ('tamanno', models.CharField(max_length=20, verbose_name='Tamaño:', db_column='Tamanno')),
                ('tipo_obra', models.CharField(max_length=20, verbose_name='Tipo de obra:', db_column='Tipo_Obra')),
                ('institucion', models.CharField(max_length=255, verbose_name='Institucion donde se introdujo:', db_column='Institucion')),
                ('cantidad_autores', models.IntegerField(max_length=3, verbose_name='Cantidad de autores:', db_column='Cantidad_Autores')),
                ('comentario', models.CharField(max_length=255, verbose_name='Comentario:', db_column='Comentario')),
                ('fichero', models.CharField(max_length=255, verbose_name='Asociar fichero', db_column='Direccion_Fichero_Asociado')),
            ],
            options={
                'verbose_name': 'Patente',
                'verbose_name_plural': 'Patentes',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='patente',
            name='cantidad_autores',
            field=models.IntegerField(max_length=3, verbose_name='Cantidad de autores:', db_column='Cantidad_Autores'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patente',
            name='ciencia_obra',
            field=models.CharField(max_length=100, verbose_name='Ciencia de la obra:', db_column='Ciencia_Obra'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patente',
            name='fuente_registro',
            field=models.CharField(max_length=100, verbose_name='Fuente:', db_column='Fuente'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patente',
            name='tipo_obra',
            field=models.CharField(max_length=50, verbose_name='Tipo de obra:', db_column='Tipo_Obra'),
            preserve_default=True,
        ),
    ]
