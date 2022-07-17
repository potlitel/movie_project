# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0055_auto_20150717_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyectoidi',
            name='area_ejecutora',
        ),
        migrations.RemoveField(
            model_name='proyectoidi',
            name='nombre',
        ),
        #migrations.RemoveField(
         #   model_name='proyectoidi',
         #   name='photos',
        #),
        migrations.AlterField(
            model_name='noticia',
            name='contenido',
            field=models.CharField(max_length=255, verbose_name='Contenido:', db_column='Contenido_Noticia'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='fichero',
            field=models.FileField(max_length=255, verbose_name='Asociar fichero', db_column='Direccion_Fichero_Adjunto', upload_to='FileSampleApp/Noticia'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='propietario',
            field=models.CharField(max_length=128, verbose_name='Propietario:', db_column='Propietario'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='titular',
            field=models.CharField(max_length=255, unique=True, verbose_name='Titular:', db_column='Titular'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ponenciaevento',
            name='propietario',
            field=models.CharField(max_length=128, verbose_name='Propietario:', db_column='Propietario'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='premio',
            name='anno',
            field=models.PositiveIntegerField(max_length=4, validators=[django.core.validators.MaxValueValidator(3000), django.core.validators.MinValueValidator(1)], default=1, verbose_name='Año:', db_column='Anno'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='premio',
            name='autor',
            field=models.CharField(max_length=255, verbose_name='Autor:', db_column='Autor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='premio',
            name='fichero',
            field=models.FileField(max_length=255, verbose_name='Asociar fichero', db_column='Direccion_Fichero_Asociado', upload_to='FileSampleApp/Premio'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='premio',
            name='lugar_premio',
            field=models.CharField(max_length=20, verbose_name='Lugar del premio:', db_column='Lugar_Premio'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='premio',
            name='propietario',
            field=models.CharField(max_length=128, verbose_name='Propietario:', db_column='Propietario'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='premio',
            name='titulo',
            field=models.CharField(max_length=255, verbose_name='Titulo:', db_column='Titulo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultadointroducido',
            name='comentario',
            field=models.CharField(max_length=255, verbose_name='Comentario:', db_column='Comentario'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultadointroducido',
            name='fichero',
            field=models.FileField(max_length=255, verbose_name='Asociar fichero', db_column='Direccion_Fichero_Asociado', upload_to='FileSampleApp/ResultadoIntroducido'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultadointroducido',
            name='institucion',
            field=models.CharField(max_length=255, verbose_name='Institucion donde se introdujo:', db_column='Institucion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultadointroducido',
            name='nombre_obra',
            field=models.CharField(max_length=255, verbose_name='Nombre de la obra:', db_column='Nombre_Obra'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultadointroducido',
            name='propietario',
            field=models.CharField(max_length=128, verbose_name='Propietario:', db_column='Propietario'),
            preserve_default=True,
        ),
    ]
