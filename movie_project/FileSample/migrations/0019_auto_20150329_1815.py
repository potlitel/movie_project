# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0018_auto_20150329_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='aprobacion',
            field=models.BooleanField(max_length=1000, verbose_name='Aprobacion', db_column='Aprobacion', default='False'),
            preserve_default=True,
        ),
    ]
