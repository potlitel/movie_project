# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0076_auto_20151206_2234'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together=set([]),
        ),
    ]
