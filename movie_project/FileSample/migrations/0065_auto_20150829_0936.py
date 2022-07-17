# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0064_auto_20150829_0934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyectoidi',
            name='area_ejecutora',
        ),
        migrations.RemoveField(
            model_name='proyectoidi',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='proyectoidi',
            name='photos',
        ),
    ]
