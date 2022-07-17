# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0006_file_datetimefiel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='datetimefiel',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
