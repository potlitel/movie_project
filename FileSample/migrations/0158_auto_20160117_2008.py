# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0157_auto_20160117_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitacion',
            name='institucion',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z- ]*$', 'Has introducido caracteres incorrectos.')], db_column='Institucion', max_length=255, verbose_name='Institución:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='capacitacion',
            name='nombre',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z- ]*$', 'Has introducido caracteres incorrectos.')], db_column='Nombre', max_length=255, verbose_name='Nombre:'),
            preserve_default=True,
        ),
        # migrations.AlterField(
            # model_name='profile',
            # name='anno_graduado',
            # field=models.DateField(default=0),
            # preserve_default=True,
        # ),
    ]
