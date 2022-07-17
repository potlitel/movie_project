# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0050_auto_20150627_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ponenciaevento',
            name='titulo',
            field=models.CharField(verbose_name='Titulo:', db_column='Titulo', max_length=255),
            preserve_default=True,
        ),
    ]
