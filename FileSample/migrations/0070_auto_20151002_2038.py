# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0069_auto_20150830_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleoestudiantes',
            name='nombre_obra',
            field=models.CharField(verbose_name='Nombre de la Obra:', db_column='Obra_CientificaID_Obra_Cientifica', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='empleoestudiantes',
            name='propietario',
            field=models.CharField(verbose_name='Propietario:', db_column='Propietario', max_length=128),
            preserve_default=True,
        ),
    ]
