# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import any_imagefield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0004_file_year_in_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='anyimage',
            field=any_imagefield.models.fields.AnyImageField(default=datetime.datetime(2015, 3, 24, 19, 52, 38, 390625, tzinfo=utc), upload_to='FileSampleApp/', verbose_name='Any image field'),
            preserve_default=False,
        ),
    ]
