# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0027_premio'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpleoEstudiantes',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('propietario', models.CharField(verbose_name='Propietario:', max_length=128, db_column='Propietario')),
                ('fuente', models.CharField(verbose_name='Fuente:', max_length=25, db_column='Tipo_Fuente')),
                ('nombre_fuente', models.CharField(verbose_name='Nombre de la Fuente:', max_length=150, db_column='Nombre_Fuente')),
                ('nombre_obra', models.IntegerField(verbose_name='Nombre de la Obra:', max_length=10, db_column='Obra_CientificaID_Obra_Cientifica')),
                ('cantidad_estudiantes', models.IntegerField(verbose_name='Cantidad de estudiantes:', max_length=10, db_column='Cantidad_Estudiantes')),
                ('fichero', models.CharField(verbose_name='Asociar fichero', max_length=255, db_column='Direccion_Fichero_Asociado')),
            ],
            options={
                'verbose_name': 'Empleo de Estudiante',
                'verbose_name_plural': 'Empleo de Estudiantes',
            },
            bases=(models.Model,),
        ),
    ]
