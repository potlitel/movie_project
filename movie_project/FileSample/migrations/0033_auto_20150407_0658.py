# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0032_auto_20150407_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitacion',
            name='institucion',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], max_length=255, db_column='Institucion', verbose_name='Institucion:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='capacitacion',
            name='nombre',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], max_length=255, db_column='Nombre', verbose_name='Nombre:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='capacitacion',
            name='propietario',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], max_length=128, db_column='Propietario', verbose_name='Propietario:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ponenciaevento',
            name='propietario',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], max_length=128, db_column='Propietario', verbose_name='Propietario:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ponenciaevento',
            name='titulo',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], max_length=255, db_column='Titulo', verbose_name='Titulo:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyectoidi',
            name='propietario',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], max_length=128, db_column='Propietario', verbose_name='Propietario:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyectoidi',
            name='titulo',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], max_length=255, db_column='Titulo', verbose_name='Titulo:'),
            preserve_default=True,
        ),
    ]
