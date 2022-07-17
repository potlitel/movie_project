# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0110_auto_20160102_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='proyectoIDi',
            field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultadointroducido',
            name='ciencia_obra',
            field=models.ForeignKey(to='FileSample.CienciaObra'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultadointroducido',
            name='tamanno',
            field=models.ForeignKey(to='FileSample.TamañoObra'),
            preserve_default=True,
        ),
    ]
