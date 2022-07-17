# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0121_auto_20160102_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleoestudiantes',
            name='nombre_obra',
            field=models.ForeignKey(to='FileSample.ObraCientifica'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membership',
            name='proyectoIDi',
            field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            preserve_default=True,
        ),
    ]
