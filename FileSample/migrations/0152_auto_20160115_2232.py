# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc

class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0151_rol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='department',
        ),
        migrations.AddField(
            model_name='profile',
            name='anno_graduado',
            field=models.DateField(default=datetime.datetime(2016, 1, 3, 18, 23, 32, 31250, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='cargo',
            field=models.ForeignKey(default=0, to='FileSample.Cargo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='carne_identidad',
            field=models.CharField(default=0, db_column='Carne_Identidad', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='categoria_docente',
            field=models.ForeignKey(default=0, to='FileSample.CategoriaDocente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='direccion',
            field=models.CharField(default=0, db_column='Direccion_Particular', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='edad',
            field=models.CharField(default=0, db_column='Edad', max_length=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='especialidad_graduado',
            field=models.CharField(default='0', db_column='Especialidad_Graduado', max_length=144),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='expediente',
            field=models.PositiveIntegerField(default=0, db_column='ID_Expediente', verbose_name='Volumen:', max_length=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='grado_cientifico',
            field=models.ForeignKey(default=0, to='FileSample.GradoCientifico'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='grupo',
            field=models.ForeignKey(default=0, to='FileSample.Grupo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='municipio',
            field=models.ForeignKey(default=0, to='FileSample.Municipio'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='provincia',
            field=models.ForeignKey(default=0, to='FileSample.Provincia'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='rol_saisa',
            field=models.ForeignKey(default=0, to='FileSample.Rol'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='sexo',
            field=models.ForeignKey(default=0, to='FileSample.Sexo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='solapin',
            field=models.CharField(default='0', unique=True, db_column='Numero_Solapin', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='titulo_academico',
            field=models.ForeignKey(default=0, to='FileSample.TituloAcademico'),
            preserve_default=True,
        ),
    ]
