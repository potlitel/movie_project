# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0037_auto_20150620_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeloyoamel',
            name='data_title',
            field=models.CharField(db_column='data_title', max_length=255, verbose_name='data_title (Titulo):'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='modeloyoamel',
            name='href',
            field=models.CharField(db_column='href', max_length=128, verbose_name='href (Relacionado con):'),
            preserve_default=True,
        ),
    ]
