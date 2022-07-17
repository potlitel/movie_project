# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0136_auto_20160103_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sai',
            name='aprobacion',
            field=models.NullBooleanField(default='False', db_column='Aprobacion', max_length=1000, verbose_name='Aprobacion:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='aprobador_SAI',
            field=models.ForeignKey(related_name='Aprobador SAI', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='aprobador_cargo_SAI',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='cargo_solicitante',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='comentario_SAI_No_Aprobacion',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='comentario_SAI_evaluacion',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='email_solicitante',
            field=models.EmailField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='evaluacion_SAI',
            field=models.ForeignKey(blank=True, to='FileSample.EvaluacionSAI'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='nombre_solicitante',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='responsable_ejecucion_SAI',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='solapin_solicitante',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='telefono_solicitante',
            field=models.PositiveIntegerField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
