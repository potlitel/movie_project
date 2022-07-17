# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0036_modeloyoamel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeloyoamel',
            name='data_description',
            field=models.CharField(verbose_name='data_description (Descripción):', max_length=255, db_column='data_description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='modeloyoamel',
            name='img',
            field=models.CharField(verbose_name='Img (Imagen pequeña):', max_length=255, db_column='Img'),
            preserve_default=True,
        ),
    ]
