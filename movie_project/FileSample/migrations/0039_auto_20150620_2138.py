# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0038_auto_20150620_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeloyoamel',
            name='data_largesrc',
            field=models.ImageField(upload_to='FileSampleApp/', db_column='data_largesrc'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='modeloyoamel',
            name='data_title',
            field=models.ImageField(upload_to='FileSampleApp/', db_column='data_title'),
            preserve_default=True,
        ),
    ]
