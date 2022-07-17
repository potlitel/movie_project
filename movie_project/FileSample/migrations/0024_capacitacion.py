# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0023_proyectoidi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capacitacion',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('propietario', models.CharField(max_length=128, db_column='Propietario', verbose_name='Propietario:')),
                ('nombre', models.CharField(max_length=255, db_column='Nombre', verbose_name='Nombre:')),
                ('tipo', models.CharField(max_length=15, db_column='Tipo', verbose_name='Tipo:')),
                ('fecha', models.DateField()),
                ('rol', models.CharField(max_length=20, db_column='Rol', verbose_name='Rol:')),
                ('modalidad', models.CharField(max_length=50, db_column='Modalidad', verbose_name='Modalidad:')),
                ('institucion', models.CharField(max_length=255, db_column='Institucion', verbose_name='Institucion:')),
                ('pais', models.CharField(max_length=50, db_column='Pais', verbose_name='Pais:')),
                ('ciudad', models.CharField(max_length=50, db_column='Ciudad', verbose_name='Ciudad:')),
                ('fichero', models.CharField(max_length=255, db_column='Direccion_Fichero_Asociado', verbose_name='Asociar fichero')),
            ],
            options={
                'verbose_name_plural': 'Capacitaciones',
                'verbose_name': 'Capacitacion',
            },
            bases=(models.Model,),
        ),
    ]
