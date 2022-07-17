# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0115_auto_20160102_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleoestudiantes',
            name='fuente',
            field=models.ForeignKey(to='FileSample.Fuente'),
            preserve_default=True,
        ),
    ]
