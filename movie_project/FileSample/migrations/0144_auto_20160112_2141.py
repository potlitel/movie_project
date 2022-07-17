# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FileSample', '0143_auto_20160110_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='capacitacion',
            name='estudiantes',
            field=models.ManyToManyField(related_name='Estudiantes_Capacitacion', to=settings.AUTH_USER_MODEL, db_table='Item_Capacitacion_Estudiantes'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='capacitacion',
            name='profesores',
            field=models.ManyToManyField(related_name='Profesores_Capacitacion', to=settings.AUTH_USER_MODEL, db_table='Item_Capacitacion_Profesores'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membership',
            name='proyectoIDi',
            field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membresia',
            name='proyectoIDi',
            field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            preserve_default=True,
        ),
    ]
