# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0114_auto_20160102_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premio',
            name='caracter',
            field=models.ForeignKey(to='FileSample.CaracterPremio'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='premio',
            name='lugar_premio',
            field=models.ForeignKey(to='FileSample.LugarPremio'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='premio',
            name='nivel_autoria',
            field=models.ForeignKey(to='FileSample.NivelAutoria'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='premio',
            name='nivel_premio',
            field=models.ForeignKey(to='FileSample.NivelEvento'),
            preserve_default=True,
        ),
    ]
