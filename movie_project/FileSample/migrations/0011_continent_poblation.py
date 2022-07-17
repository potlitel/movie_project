# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0010_auto_20150327_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='continent',
            name='poblation',
            field=models.CharField(max_length=128, verbose_name='Item poblation: ', default=1234),
            preserve_default=False,
        ),
    ]
