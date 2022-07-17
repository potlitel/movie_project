# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0045_auto_20150627_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='ciudad',
            field=models.CharField(verbose_name='Ciudad:', max_length=30, db_column='Ciudad'),
            preserve_default=True,
        ),
    ]
