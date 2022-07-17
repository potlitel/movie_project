# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0043_auto_20150627_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='anno',
            field=models.CharField(max_length=10, verbose_name='Año:', db_column='Anno'),
            preserve_default=True,
        ),
    ]
