# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='File',
            field=models.FileField(upload_to='FileSample'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='file',
            name='image',
            field=models.ImageField(upload_to='FileSample'),
            preserve_default=True,
        ),
    ]
