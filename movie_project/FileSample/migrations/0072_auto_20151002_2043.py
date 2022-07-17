# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0071_auto_20151002_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleoestudiantes',
            name='fuente',
            field=models.CharField(max_length=40, db_column='Tipo_Fuente', verbose_name='Fuente:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membership',
            name='proyectoIDi',
            field=models.ForeignKey(to='FileSample.ProyectoIDI'),
            preserve_default=True,
        ),
    ]
