# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0107_auto_20160102_1127'),
    ]

    operations = [
        # migrations.AlterField(
            # model_name='membership',
            # name='proyectoIDi',
            # field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            # preserve_default=True,
        # ),
        migrations.AlterField(
            model_name='ponenciaevento',
            name='nivel_autoria',
            field=models.ForeignKey(to='FileSample.NivelAutoria'),
            preserve_default=True,
        ),
    ]
