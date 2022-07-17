# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0021_auto_20150330_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='PonenciaEvento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('propietario', models.CharField(max_length=128, verbose_name='Propietario:', db_column='Propietario')),
                ('titulo', models.CharField(max_length=255, verbose_name='Titulo:', db_column='Titulo')),
                ('autor', models.CharField(max_length=20, verbose_name='Autor:', db_column='Autor')),
                ('nivel_autoria', models.CharField(max_length=20, verbose_name='Pais:', db_column='Pais')),
                ('fichero', models.CharField(max_length=255, verbose_name='Asociar fichero', db_column='Direccion_Fichero_Asociado')),
                ('evento', models.ForeignKey(to='FileSample.Evento')),
            ],
            options={
                'verbose_name_plural': 'Ponencias en eventos',
                'verbose_name': 'Ponencia en evento',
            },
            bases=(models.Model,),
        ),
    ]
