# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0079_auto_20151213_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='ciudad',
            field=models.ForeignKey(to='FileSample.Ciudad'),
            preserve_default=True,
        ),
    ]
