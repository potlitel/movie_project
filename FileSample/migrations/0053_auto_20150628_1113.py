# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0052_auto_20150628_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitacion',
            name='institucion',
            field=models.CharField(verbose_name='Institucion:', max_length=255, db_column='Institucion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='capacitacion',
            name='nombre',
            field=models.CharField(verbose_name='Nombre:', max_length=255, db_column='Nombre'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='capacitacion',
            name='propietario',
            field=models.CharField(verbose_name='Propietario:', max_length=128, db_column='Propietario'),
            preserve_default=True,
        ),
    ]
