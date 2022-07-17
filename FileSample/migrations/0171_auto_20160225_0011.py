# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0170_auto_20160224_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='premio',
            name='obracientifica',
            field=models.ForeignKey(null=True, to='FileSample.ObraCientifica', verbose_name='Obra Científica a premiar:'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='premio',
            name='ponenciaevento',
            field=models.ForeignKey(null=True, to='FileSample.PonenciaEvento', verbose_name='Ponencia a premiar:'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='premio',
            name='proyecto',
            field=models.ForeignKey(null=True, to='FileSample.ProyectoiDi', verbose_name='Proyecto a premiar:'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='premio',
            name='publicacion',
            field=models.ForeignKey(null=True, to='FileSample.Publicacion', verbose_name='Publicación a premiar:'),
            preserve_default=True,
        ),
        # migrations.AlterField(
            # model_name='profile',
            # name='anno_graduado',
            # field=models.DateField(default=0),
            # preserve_default=True,
        # ),
    ]
