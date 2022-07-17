# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0026_auto_20150403_0749'),
    ]

    operations = [
        migrations.CreateModel(
            name='Premio',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('propietario', models.CharField(db_column='Propietario', max_length=128, verbose_name='Propietario:')),
                ('titulo', models.CharField(db_column='Titulo', max_length=255, verbose_name='Titulo:')),
                ('autor', models.CharField(db_column='Autor', max_length=255, verbose_name='Autor:')),
                ('nivel_autoria', models.CharField(db_column='Nivel_Autoria', max_length=20, verbose_name='Nivel de autoria:')),
                ('anno', models.CharField(db_column='Anno', max_length=4, verbose_name='Año:')),
                ('pais', models.CharField(db_column='Pais', max_length=50, verbose_name='Pais:')),
                ('ciudad', models.CharField(db_column='Ciudad', max_length=50, verbose_name='Ciudad:')),
                ('lugar_premio', models.CharField(db_column='Lugar_Premio', max_length=5, verbose_name='Lugar del premio:')),
                ('nivel_premio', models.CharField(db_column='Nivel', max_length=20, verbose_name='Nivel:')),
                ('caracter', models.CharField(db_column='Caracter', max_length=20, verbose_name='Caracter:')),
                ('fichero', models.CharField(db_column='Direccion_Fichero_Asociado', max_length=255, verbose_name='Asociar fichero')),
            ],
            options={
                'verbose_name_plural': 'Premios',
                'verbose_name': 'Premio',
            },
            bases=(models.Model,),
        ),
    ]
