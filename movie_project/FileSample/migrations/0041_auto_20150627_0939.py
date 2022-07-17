# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0040_auto_20150620_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeloyoamel',
            name='data_largesrc',
            field=models.ImageField(upload_to='FileSampleApp/Yoamel', db_column='data_largesrc'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='modeloyoamel',
            name='img',
            field=models.ImageField(upload_to='FileSampleApp/Yoamel', db_column='Img'),
            preserve_default=True,
        ),
    ]
