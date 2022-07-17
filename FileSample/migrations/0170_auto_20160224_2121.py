# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0169_auto_20160224_2030'),
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
            model_name='patente',
            name='nombre_obra',
            field=models.ForeignKey(to='FileSample.ObraCientifica'),
            preserve_default=True,
        ),
        # migrations.AlterField(
            # model_name='profile',
            # name='anno_graduado',
            # field=models.DateField(default=0),
            # preserve_default=True,
        # ),
        migrations.AlterField(
            model_name='resultadointroducido',
            name='nombre_obra',
            field=models.ForeignKey(to='FileSample.ObraCientifica'),
            preserve_default=True,
        ),
    ]
