# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0002_auto_20150311_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='File',
            field=models.FileField(upload_to='FileSampleApp/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='file',
            name='image',
            field=models.ImageField(upload_to='FileSampleApp/'),
            preserve_default=True,
        ),
    ]
