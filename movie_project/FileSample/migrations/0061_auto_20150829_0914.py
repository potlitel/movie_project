# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0060_auto_20150829_0905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date_joined', models.DateField()),
                ('invite_reason', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProyectoIDi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('propietario', models.CharField(verbose_name='Propietario:', max_length=128, db_column='Propietario')),
                ('titulo', models.CharField(verbose_name='Titulo:', max_length=255, db_column='Titulo')),
                ('nivel', models.CharField(verbose_name='Nivel:', max_length=15, db_column='Nivel')),
                ('linea_cientifica', models.CharField(verbose_name='Linea cientifica:', max_length=255, db_column='Linea_Cientifica')),
                ('rol', models.CharField(verbose_name='Rol:', max_length=255, db_column='Rol')),
                ('fichero', models.FileField(verbose_name='Asociar fichero', max_length=255, db_column='Direccion_Fichero_Asociado', upload_to='FileSampleApp/ProjectoIdi')),
                ('area_ejecutora', models.ForeignKey(to='FileSample.PonenciaEvento')),
                ('nombre', models.ForeignKey(to='FileSample.Evento')),
                ('publicaciones', models.ManyToManyField(through='FileSample.Membership', to='FileSample.Publicacion')),
            ],
            options={
                'verbose_name': 'Proyecto IDi',
                'verbose_name_plural': 'Proyectos IDi',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='membership',
            name='proyectoIDi',
            field=models.ForeignKey(to='FileSample.ProyectoIDi'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membership',
            name='publicacion',
            field=models.ForeignKey(to='FileSample.Publicacion'),
            preserve_default=True,
        ),
    ]
