# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0063_auto_20150829_0931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyectoidi',
            old_name='publicaciones',
            new_name='photos',
        ),
    ]
