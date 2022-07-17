# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0081_auto_20151215_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='ciudad',
            field=models.ForeignKey(to='FileSample.Ciudad'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='pais',
            field=models.ForeignKey(to='FileSample.Pais'),
            preserve_default=True,
        ),
    ]
