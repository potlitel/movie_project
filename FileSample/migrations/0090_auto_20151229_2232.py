# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0089_auto_20151229_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='obracientifica',
            name='fichero',
            field=models.FileField(max_length=255, db_column='Direccion_Fichero_Adjunto', default=datetime.datetime(2015, 12, 30, 3, 32, 58, 31250, tzinfo=utc), upload_to='FileSampleApp/ObraCientifica', verbose_name='Asociar fichero'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='membership',
            name='proyectoIDi',
            field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            preserve_default=True,
        ),
    ]
