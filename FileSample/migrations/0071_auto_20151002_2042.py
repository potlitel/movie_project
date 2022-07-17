# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0070_auto_20151002_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleoestudiantes',
            name='fichero',
            field=models.FileField(db_column='Direccion_Fichero_Asociado', max_length=255, upload_to='FileSampleApp/EmpleoEstudiantes', verbose_name='Asociar fichero'),
            preserve_default=True,
        ),
    ]
