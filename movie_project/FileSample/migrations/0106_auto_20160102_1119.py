# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0105_auto_20160101_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='nivel_autoria',
            field=models.ForeignKey(to='FileSample.NivelAutoria'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='nivel_mes',
            field=models.ForeignKey(to='FileSample.NivelMES'),
            preserve_default=True,
        ),
    ]
