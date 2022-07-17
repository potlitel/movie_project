# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0167_auto_20160223_2313'),
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
        migrations.AlterField(
            model_name='noticia',
            name='contenido',
            field=models.CharField(db_column='Contenido_Noticia', max_length=2555, validators=[django.core.validators.RegexValidator('^[a-zA-Z- .,;]*$', 'Has introducido caracteres incorrectos.')], verbose_name='Contenido:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='titular',
            field=models.CharField(db_column='Titular', max_length=255, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z- .,;]*$', 'Only alphanumeric characters are allowed.')], verbose_name='Titular:', unique=True),
            preserve_default=True,
        ),
        # migrations.AlterField(
            # model_name='profile',
            # name='anno_graduado',
            # field=models.DateField(default=0),
            # preserve_default=True,
        # ),
    ]
