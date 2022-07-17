# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0153_auto_20160117_1935'),
    ]

    operations = [
        # migrations.AlterField(
            # model_name='membresia',
            # name='proyectoIDi',
            # field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            # preserve_default=True,
        # ),
        migrations.AlterField(
            model_name='obracientifica',
            name='descripcion',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z- .,;]*$', 'Has introducido caracteres incorrectos.')], verbose_name='Descripción', db_column='Descripcion', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='obracientifica',
            name='titulo',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z- ]*$', 'Has introducido caracteres incorrectos.')], verbose_name='Título', db_column='Titulo', max_length=128, unique=True),
            preserve_default=True,
        ),
        # migrations.AlterField(
            # model_name='profile',
            # name='anno_graduado',
            # field=models.DateField(default=0),
            # preserve_default=True,
        # ),
    ]
