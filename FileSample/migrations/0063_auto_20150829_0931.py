# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0062_auto_20150829_0928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyectoidi',
            old_name='nombre1',
            new_name='nombre',
        ),
    ]
