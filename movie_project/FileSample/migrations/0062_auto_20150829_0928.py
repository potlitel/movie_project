# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0061_auto_20150829_0914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyectoidi',
            old_name='nombre',
            new_name='nombre1',
        ),
    ]
