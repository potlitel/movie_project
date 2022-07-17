# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0128_auto_20160103_1328'),
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
            model_name='proyectoidi',
            name='linea_cientifica',
            field=models.ForeignKey(to='FileSample.LineaCientificaProyecto'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyectoidi',
            name='nivel',
            field=models.ForeignKey(to='FileSample.NivelProyecto'),
            preserve_default=True,
        ),
    ]
