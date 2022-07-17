# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0155_auto_20160117_1955'),
    ]

    operations = [
        # migrations.AlterField(
            # model_name='membership',
            # name='proyectoIDi',
            # field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            # preserve_default=True,
        # ),
        # migrations.AlterField(
            # model_name='membresia',
            # name='proyectoIDi',
            # field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            # preserve_default=True,
        # ),
        # migrations.AlterField(
            # model_name='profile',
            # name='anno_graduado',
            # field=models.DateField(default=0),
            # preserve_default=True,
        # ),
        migrations.AlterField(
            model_name='resultadointroducido',
            name='comentario',
            field=models.CharField(verbose_name='Comentario:', db_column='Comentario', max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z- .,;]*$', 'Has introducido caracteres incorrectos.')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultadointroducido',
            name='institucion',
            field=models.CharField(verbose_name='Institución donde se introdujo:', db_column='Institucion', max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z- ]*$', 'Has introducido caracteres incorrectos.')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultadointroducido',
            name='nombre_obra',
            field=models.CharField(verbose_name='Nombre de la obra:', db_column='Nombre_Obra', max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z- ]*$', 'Has introducido caracteres incorrectos.')]),
            preserve_default=True,
        ),
    ]
