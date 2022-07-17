# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0086_auto_20151216_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='proyectoIDi',
            field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='premio',
            name='ciudad',
            field=models.ForeignKey(to='FileSample.Ciudad'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='premio',
            name='pais',
            field=models.ForeignKey(to='FileSample.Pais'),
            preserve_default=True,
        ),
    ]
