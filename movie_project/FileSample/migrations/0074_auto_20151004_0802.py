# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0073_auto_20151002_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyectoidi',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='proyectoidi',
            name='rol',
        ),
    ]
