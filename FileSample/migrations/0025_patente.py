# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0024_capacitacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propietario', models.CharField(max_length=128, db_column='Propietario', verbose_name='Propietario:')),
                ('nombre_obra', models.CharField(max_length=255, db_column='Nombre_Obra', verbose_name='Nombre de la obra:')),
                ('ciencia_obra', models.CharField(max_length=15, db_column='Ciencia_Obra', verbose_name='Ciencia de la obra:')),
                ('fecha', models.DateField()),
                ('tipo_obra', models.CharField(max_length=20, db_column='Tipo_Obra', verbose_name='Tipo de obra:')),
                ('fuente_registro', models.CharField(max_length=20, db_column='Fuente', verbose_name='Fuente:')),
                ('cantidad_autores', models.IntegerField(max_length=50, db_column='Cantidad_Autores', verbose_name='Cantidad de autores:')),
                ('comentario', models.CharField(max_length=255, db_column='Comentario', verbose_name='Comentario:')),
                ('fichero', models.CharField(max_length=255, db_column='Direccion_Fichero_Asociado', verbose_name='Asociar fichero')),
            ],
            options={
                'verbose_name_plural': 'Patentes',
                'verbose_name': 'Patente',
            },
            bases=(models.Model,),
        ),
    ]
