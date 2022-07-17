# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0005_file_anyimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='datetimefiel',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 24, 20, 5, 57, 921875, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
