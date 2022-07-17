# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0137_auto_20160104_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membresia',
            name='proyectoIDi',
            field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='aprobador_SAI',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, related_name='Aprobador SAI'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='evaluacion_SAI',
            field=models.ForeignKey(null=True, to='FileSample.EvaluacionSAI'),
            preserve_default=True,
        ),
    ]
