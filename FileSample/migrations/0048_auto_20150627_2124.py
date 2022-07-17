# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0047_auto_20150627_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='ciudad',
            field=models.CharField(db_column='Ciudad', verbose_name='Ciudad:', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='pais',
            field=models.CharField(db_column='Pais', verbose_name='Pais:', max_length=30),
            preserve_default=True,
        ),
    ]
