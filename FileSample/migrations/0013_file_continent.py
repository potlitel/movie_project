# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0012_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='continent',
            field=models.CharField(default=datetime.datetime(2015, 3, 28, 1, 20, 48, 562500, tzinfo=utc), max_length=20, verbose_name='Name'),
            preserve_default=False,
        ),
    ]
