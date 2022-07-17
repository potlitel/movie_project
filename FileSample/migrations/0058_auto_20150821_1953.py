# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0057_auto_20150719_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='contenido',
            field=models.CharField(db_column='Contenido_Noticia', verbose_name='Contenido:', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='fichero',
            field=models.FileField(db_column='Direccion_Fichero_Adjunto', verbose_name='Asociar fichero', max_length=255, upload_to='FileSampleApp/Noticia'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='propietario',
            field=models.CharField(db_column='Propietario', verbose_name='Propietario:', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='titular',
            field=models.CharField(db_column='Titular', unique=True, verbose_name='Titular:', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ponenciaevento',
            name='propietario',
            field=models.CharField(db_column='Propietario', verbose_name='Propietario:', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='premio',
            name='anno',
            field=models.PositiveIntegerField(default=1, db_column='Anno', verbose_name='Año:', validators=[django.core.validators.MaxValueValidator(3000), django.core.validators.MinValueValidator(1)], max_length=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='premio',
            name='autor',
            field=models.CharField(db_column='Autor', verbose_name='Autor:', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='premio',
            name='fichero',
            field=models.FileField(db_column='Direccion_Fichero_Asociado', verbose_name='Asociar fichero', max_length=255, upload_to='FileSampleApp/Premio'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='premio',
            name='lugar_premio',
            field=models.CharField(db_column='Lugar_Premio', verbose_name='Lugar del premio:', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='premio',
            name='propietario',
            field=models.CharField(db_column='Propietario', verbose_name='Propietario:', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='premio',
            name='titulo',
            field=models.CharField(db_column='Titulo', verbose_name='Titulo:', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultadointroducido',
            name='comentario',
            field=models.CharField(db_column='Comentario', verbose_name='Comentario:', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultadointroducido',
            name='fichero',
            field=models.FileField(db_column='Direccion_Fichero_Asociado', verbose_name='Asociar fichero', max_length=255, upload_to='FileSampleApp/ResultadoIntroducido'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultadointroducido',
            name='institucion',
            field=models.CharField(db_column='Institucion', verbose_name='Institucion donde se introdujo:', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultadointroducido',
            name='nombre_obra',
            field=models.CharField(db_column='Nombre_Obra', verbose_name='Nombre de la obra:', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultadointroducido',
            name='propietario',
            field=models.CharField(db_column='Propietario', verbose_name='Propietario:', max_length=128),
            preserve_default=True,
        ),
    ]
