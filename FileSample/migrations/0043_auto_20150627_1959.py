# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0042_auto_20150627_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='editorial',
            field=models.CharField(db_column='Editorial', verbose_name='Editorial:', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='propietario',
            field=models.CharField(db_column='Propietario', verbose_name='Propietario:', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='publicacion',
            field=models.CharField(db_column='Publicacion', verbose_name='Publicacion:', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='titulo',
            field=models.CharField(db_column='Titulo', verbose_name='Titulo:', max_length=255),
            preserve_default=True,
        ),
    ]
