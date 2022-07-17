# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0078_auto_20151206_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='proyectoIDi',
            field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='ciudad',
            field=models.CharField(max_length=30, db_column='Ciudad', verbose_name='Ciudad:'),
            preserve_default=True,
        ),
    ]
