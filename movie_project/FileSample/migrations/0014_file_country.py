# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0013_file_continent'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='country',
            field=models.CharField(max_length=20, verbose_name='Name', default=datetime.datetime(2015, 3, 28, 11, 43, 28, 218750, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
