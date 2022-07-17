# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0048_auto_20150627_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='nombre',
            field=models.CharField(verbose_name='Nombre:', db_column='Nombre', max_length=255),
            preserve_default=True,
        ),
    ]
