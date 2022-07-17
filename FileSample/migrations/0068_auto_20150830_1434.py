# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0067_auto_20150830_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyectoidi',
            name='area_ejecutora',
            field=models.ForeignKey(to='FileSample.PonenciaEvento', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proyectoidi',
            name='nombre',
            field=models.ForeignKey(to='FileSample.Evento', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proyectoidi',
            name='publicaciones',
            field=models.ManyToManyField(to='FileSample.Publicacion', through='FileSample.Membership'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membership',
            name='proyectoIDi',
            field=models.ForeignKey(to='FileSample.ProyectoIDI'),
            preserve_default=True,
        ),
    ]
