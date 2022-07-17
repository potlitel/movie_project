# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0138_auto_20160104_2324'),
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
            name='responsable_ejecucion_SAI',
            field=models.ForeignKey(null=True, related_name='Responsable Ejecucion SAI', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
