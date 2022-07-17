# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0120_auto_20160102_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultadointroducido',
            name='tipo_obra',
            field=models.ForeignKey(to='FileSample.TipoObraCientifica'),
            preserve_default=True,
        ),
    ]
