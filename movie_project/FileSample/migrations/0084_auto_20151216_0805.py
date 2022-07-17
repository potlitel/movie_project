# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0083_auto_20151215_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitacion',
            name='ciudad',
            field=models.ForeignKey(to='FileSample.Ciudad'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='capacitacion',
            name='pais',
            field=models.ForeignKey(to='FileSample.Pais'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membership',
            name='proyectoIDi',
            field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            preserve_default=True,
        ),
    ]
