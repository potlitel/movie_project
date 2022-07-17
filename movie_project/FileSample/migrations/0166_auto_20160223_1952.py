# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FileSample', '0165_auto_20160223_0730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='premio',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='premio',
            name='nivel_autoria',
        ),
        migrations.AddField(
            model_name='premio',
            name='autores',
            field=models.ManyToManyField(related_name='Premio_Autores', to=settings.AUTH_USER_MODEL, db_table='Premio_Autores'),
            preserve_default=True,
        ),
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
