# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0056_auto_20150829_0939'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='proyectoidi',
        #     name='area_ejecutora',
        #     field=models.ForeignKey(default=datetime.datetime(2015, 8, 29, 13, 42, 22, 421875, tzinfo=utc), to='FileSample.PonenciaEvento'),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='proyectoidi',
        #     name='nombre',
        #     field=models.ForeignKey(default=datetime.datetime(2015, 8, 29, 13, 42, 29, 171875, tzinfo=utc), to='FileSample.Evento'),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='proyectoidi',
        #     name='photos',
        #     field=models.ManyToManyField(through='FileSample.Membership', to='FileSample.Publicacion'),
        #     preserve_default=True,
        # ),
    ]
