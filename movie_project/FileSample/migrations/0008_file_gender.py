# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0007_auto_20150324_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='vinyl', max_length=20, verbose_name='Years in school'),
            preserve_default=True,
        ),
    ]
