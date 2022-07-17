# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0003_auto_20150311_0530'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='year_in_school',
            field=models.CharField(default='vinyl', verbose_name='Years in school', choices=[('Audio', (('vinyl', 'Vinyl'), ('cd', 'CD'))), ('Video', (('vhs', 'VHS Tape'), ('dvd', 'DVD'))), ('unknown', 'Unknown')], max_length=20),
            preserve_default=True,
        ),
    ]
