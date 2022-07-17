# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0008_file_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='name',
            field=models.CharField(verbose_name='Name', max_length=20, default=datetime.datetime(2015, 3, 28, 0, 20, 4, 296875, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], verbose_name='Gender', max_length=20),
            preserve_default=True,
        ),
    ]
