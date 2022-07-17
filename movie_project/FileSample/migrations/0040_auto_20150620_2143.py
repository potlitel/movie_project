# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0039_auto_20150620_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeloyoamel',
            name='data_title',
            field=models.CharField(verbose_name='data_title (Titulo):', max_length=255, db_column='data_title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='modeloyoamel',
            name='img',
            field=models.ImageField(upload_to='FileSampleApp/', db_column='Img'),
            preserve_default=True,
        ),
    ]
