# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0031_auto_20150407_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='edicion',
            field=models.PositiveIntegerField(verbose_name='Numero de la edicion:', db_column='Edicion', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='nombre',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], verbose_name='Nombre:', db_column='Nombre', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='editorial',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], verbose_name='Editorial:', db_column='Editorial', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='propietario',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], verbose_name='Propietario:', db_column='Propietario', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='publicacion',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], verbose_name='Publicacion:', db_column='Publicacion', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='titulo',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], verbose_name='Titulo:', db_column='Titulo', max_length=255),
            preserve_default=True,
        ),
    ]
