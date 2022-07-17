# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0053_auto_20150628_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patente',
            name='comentario',
            field=models.CharField(max_length=255, verbose_name='Comentario:', db_column='Comentario'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patente',
            name='fichero',
            field=models.FileField(upload_to='FileSampleApp/Patente', max_length=255, verbose_name='Asociar fichero', db_column='Direccion_Fichero_Asociado'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patente',
            name='nombre_obra',
            field=models.CharField(max_length=255, verbose_name='Nombre de la obra:', db_column='Nombre_Obra'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patente',
            name='propietario',
            field=models.CharField(max_length=128, verbose_name='Propietario:', db_column='Propietario'),
            preserve_default=True,
        ),
    ]
