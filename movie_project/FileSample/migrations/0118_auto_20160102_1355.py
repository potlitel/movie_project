# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0117_auto_20160102_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obracientifica',
            name='tamanno',
            field=models.ForeignKey(to='FileSample.TamañoObra'),
            preserve_default=True,
        ),
    ]
