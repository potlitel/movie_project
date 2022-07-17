# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0119_auto_20160102_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patente',
            name='tipo_obra',
            field=models.ForeignKey(to='FileSample.TipoObraCientifica'),
            preserve_default=True,
        ),
    ]
