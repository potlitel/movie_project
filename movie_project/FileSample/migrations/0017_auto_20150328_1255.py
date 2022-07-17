# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0016_auto_20150328_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='continent',
            name='continent_name',
            field=models.CharField(max_length=128, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='country',
            name='country_name',
            field=models.CharField(max_length=128, unique=True),
            preserve_default=True,
        ),
    ]
