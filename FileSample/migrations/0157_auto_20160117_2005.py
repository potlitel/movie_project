# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0156_auto_20160117_1959'),
    ]

    operations = [
        # migrations.AlterField(
            # model_name='membership',
            # name='proyectoIDi',
            # field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            # preserve_default=True,
        # ),
        migrations.AlterField(
            model_name='patente',
            name='comentario',
            field=models.CharField(db_column='Comentario', verbose_name='Comentario:', max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z- .,;]*$', 'Has introducido caracteres incorrectos.')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patente',
            name='nombre_obra',
            field=models.CharField(db_column='Nombre_Obra', verbose_name='Nombre de la obra:', max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z- ]*$', 'Has introducido caracteres incorrectos.')]),
            preserve_default=True,
        ),
        # migrations.AlterField(
            # model_name='profile',
            # name='anno_graduado',
            # field=models.DateField(default=0),
            # preserve_default=True,
        # ),
    ]
