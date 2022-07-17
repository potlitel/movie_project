# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FileSample', '0124_auto_20160103_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='invite_reason',
            new_name='rol',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='publicacion',
        ),
        migrations.RemoveField(
            model_name='proyectoidi',
            name='publicaciones',
        ),
        migrations.AddField(
            model_name='membership',
            name='participantes',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proyectoidi',
            name='participantes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='FileSample.Membership'),
            preserve_default=True,
        ),
        # migrations.AlterField(
            # model_name='membership',
            # name='proyectoIDi',
            # field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            # preserve_default=True,
        # ),
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together=set([('participantes', 'proyectoIDi')]),
        ),
    ]
