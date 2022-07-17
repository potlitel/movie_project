# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0160_auto_20160117_2013'),
    ]

    operations = [
        # migrations.AlterField(
            # model_name='profile',
            # name='anno_graduado',
            # field=models.DateField(default=0),
            # preserve_default=True,
        # ),
        migrations.AlterField(
            model_name='publicacion',
            name='editorial',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z- ]*$', 'Has introducido caracteres incorrectos.')], verbose_name='Editorial:', db_column='Editorial'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='numero',
            field=models.PositiveIntegerField(max_length=10, verbose_name='Número:', db_column='Numero'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='publicacion',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z- ]*$', 'Has introducido caracteres incorrectos.')], verbose_name='Publicación:', db_column='Publicacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='titulo',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z- ]*$', 'Has introducido caracteres incorrectos.')], verbose_name='Titulo:', db_column='Titulo'),
            preserve_default=True,
        ),
    ]
