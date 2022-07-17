# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0126_auto_20160103_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='estado',
            field=models.CharField(max_length=64, default=datetime.datetime(2016, 1, 3, 18, 23, 32, 31250, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='membership',
            name='proyectoIDi',
            field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            preserve_default=True,
        ),
    ]
