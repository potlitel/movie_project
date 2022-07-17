# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FileSample', '0135_auto_20160103_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='sai',
            name='ejecutores',
            field=models.ManyToManyField(db_table='Ejecutores_SAI', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membership',
            name='proyectoIDi',
            field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='area_solicitante',
            field=models.CharField(db_column='Area_solicitante', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='solicitante',
            field=models.ForeignKey(related_name='Solicitante SAI', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
