# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0041_auto_20150627_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='fichero',
            field=models.FileField(max_length=255, verbose_name='Asociar fichero', upload_to='FileSampleApp/Publicacion', db_column='Direccion_Fichero_Asociado'),
            preserve_default=True,
        ),
    ]
