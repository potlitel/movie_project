# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0159_auto_20160117_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='nombre',
            field=models.CharField(verbose_name='Nombre:', max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z- ]*$', 'Has introducido caracteres incorrectos.')], db_column='Nombre'),
            preserve_default=True,
        ),
        # migrations.AlterField(
            # model_name='profile',
            # name='anno_graduado',
            # field=models.DateField(default=0),
            # preserve_default=True,
        # ),
    ]
