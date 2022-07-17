# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0129_auto_20160103_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membresia',
            name='proyectoIDi',
            field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyectoidi',
            name='propietario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='propietarioProyectoIDi'),
            preserve_default=True,
        ),
    ]
