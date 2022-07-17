# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0046_auto_20150627_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='ciudad',
            field=models.IntegerField(max_length=30, verbose_name='Ciudad:', db_column='Ciudad'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='pais',
            field=models.IntegerField(max_length=30, verbose_name='Pais:', db_column='Pais'),
            preserve_default=True,
        ),
    ]
