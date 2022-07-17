# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0093_auto_20151229_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obracientifica',
            name='propietario',
        ),
    ]
