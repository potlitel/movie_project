# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0030_auto_20150406_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premio',
            name='anno',
            field=models.PositiveIntegerField(db_column='Anno', verbose_name='Año:', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], default=1, max_length=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='editorial',
            field=models.CharField(db_column='Editorial', verbose_name='Editorial:', validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este contiene caracteres no permitidos.')], max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='propietario',
            field=models.CharField(db_column='Propietario', verbose_name='Propietario:', validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este contiene caracteres no permitidos.')], max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='publicacion',
            field=models.CharField(db_column='Publicacion', verbose_name='Publicacion:', validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este contiene caracteres no permitidos.')], max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='titulo',
            field=models.CharField(db_column='Titulo', verbose_name='Titulo:', validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este contiene caracteres no permitidos.')], max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='volumen',
            field=models.PositiveIntegerField(db_column='Volumen', verbose_name='Volumen:', max_length=10),
            preserve_default=True,
        ),
    ]
