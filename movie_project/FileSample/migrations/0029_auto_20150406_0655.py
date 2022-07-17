# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0028_empleoestudiantes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('propietario', models.CharField(db_column='Propietario', verbose_name='Propietario:', max_length=128)),
                ('titular', models.CharField(db_column='Titular', verbose_name='Titular:', unique=True, max_length=25)),
                ('rango_tiempo', models.CharField(db_column='Rango de Tiempo', verbose_name='Rango de Tiempo:', max_length=150)),
                ('publicacion', models.DateField()),
                ('tiempo_visibilidad', models.CharField(db_column='Tiempo_Visibilidad', verbose_name='Tiempo de visibilidad:', max_length=10)),
                ('caracter', models.CharField(db_column='Caracter', verbose_name='Caracter:', max_length=10)),
                ('contenido', models.CharField(db_column='Contenido_Noticia', verbose_name='Contenido:', max_length=10)),
                ('aprobacion', models.BooleanField(verbose_name='Aprobacion:', db_column='Aprobacion', default='False', max_length=1000)),
                ('fichero', models.CharField(db_column='Direccion_Fichero_Adjunto', verbose_name='Asociar fichero', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Noticias',
                'verbose_name': 'Noticia',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='empleoestudiantes',
            name='cantidad_estudiantes',
            field=models.CharField(db_column='Cantidad_Estudiantes', verbose_name='Cantidad de estudiantes:', max_length=10),
            preserve_default=True,
        ),
    ]
