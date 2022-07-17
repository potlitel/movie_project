# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0044_auto_20150627_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='ciudad',
            field=models.IntegerField(max_length=30, verbose_name='Ciudad:', db_column='Ciudad'),
            preserve_default=True,
        ),
    ]
