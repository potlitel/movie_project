# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FileSample', '0166_auto_20160223_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyectoidi',
            name='participantes',
        ),
        migrations.AddField(
            model_name='proyectoidi',
            name='miembros',
            field=models.ManyToManyField(db_table='ProyectoIDI_Miembros', to=settings.AUTH_USER_MODEL, related_name='ProyectoIDI_Miembros'),
            preserve_default=True,
        ),
        # migrations.AlterField(
            # model_name='profile',
            # name='anno_graduado',
            # field=models.DateField(default=0),
            # preserve_default=True,
        # ),
    ]
