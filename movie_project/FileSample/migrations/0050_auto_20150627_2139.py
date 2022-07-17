# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0049_auto_20150627_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ponenciaevento',
            name='fichero',
            field=models.FileField(verbose_name='Asociar fichero', db_column='Direccion_Fichero_Asociado', max_length=255, upload_to='FileSampleApp/PonenciaEvento'),
            preserve_default=True,
        ),
    ]
