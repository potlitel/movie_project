# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FileSample', '0066_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleoestudiantes',
            name='estudiantes',
            field=models.ManyToManyField(db_table='Employed_Users', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membership',
            name='proyectoIDi',
            field=models.ForeignKey(to='FileSample.ProyectoIDI'),
            preserve_default=True,
        ),
    ]
