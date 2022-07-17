# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0051_auto_20150627_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitacion',
            name='fichero',
            field=models.FileField(upload_to='FileSampleApp/Capacitacion', db_column='Direccion_Fichero_Asociado', verbose_name='Asociar fichero', max_length=255),
            preserve_default=True,
        ),
    ]
