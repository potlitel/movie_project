# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0022_ponenciaevento'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProyectoIDi',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('propietario', models.CharField(db_column='Propietario', max_length=128, verbose_name='Propietario:')),
                ('titulo', models.CharField(db_column='Titulo', max_length=255, verbose_name='Titulo:')),
                ('nivel', models.CharField(db_column='Nivel', max_length=10, verbose_name='Nivel:')),
                ('linea_cientifica', models.CharField(db_column='Linea_Cientifica', max_length=255, verbose_name='Linea cientifica:')),
                ('rol', models.CharField(db_column='Rol', max_length=255, verbose_name='Rol:')),
                ('fichero', models.CharField(db_column='Direccion_Fichero_Asociado', max_length=255, verbose_name='Asociar fichero')),
                ('area_ejecutora', models.ForeignKey(to='FileSample.PonenciaEvento')),
                ('nombre', models.ForeignKey(to='FileSample.Evento')),
            ],
            options={
                'verbose_name': 'Proyecto IDi',
                'verbose_name_plural': 'Proyectos IDi',
            },
            bases=(models.Model,),
        ),
    ]
