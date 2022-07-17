# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FileSample', '0163_auto_20160223_0018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ponenciaevento',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='ponenciaevento',
            name='nivel_autoria',
        ),
        migrations.AddField(
            model_name='ponenciaevento',
            name='autores',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, db_table='PonenciaEvento_Autores', related_name='PonenciaEvento_Autores'),
            preserve_default=True,
        ),
        # migrations.AlterField(
            # model_name='membership',
            # name='proyectoIDi',
            # field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            # preserve_default=True,
        # ),
        # migrations.AlterField(
            # model_name='membresia',
            # name='proyectoIDi',
            # field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            # preserve_default=True,
        # ),
        # migrations.AlterField(
            # model_name='profile',
            # name='anno_graduado',
            # field=models.DateField(default=0),
            # preserve_default=True,
        # ),
    ]
