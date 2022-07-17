# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0106_auto_20160102_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='nivel',
            field=models.ForeignKey(to='FileSample.NivelEvento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='tipo_publicacion',
            field=models.ForeignKey(to='FileSample.TipoPublicacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membership',
            name='proyectoIDi',
            field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            preserve_default=True,
        ),
    ]
