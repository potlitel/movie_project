# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0113_auto_20160102_1341'),
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
            name='tipo_obra',
            field=models.CharField(db_column='Tipo_Obra', verbose_name='Tipo de obra:', max_length=20),
            preserve_default=True,
        ),
    ]
