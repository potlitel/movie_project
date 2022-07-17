# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators
import datetime
from django.utils.timezone import utc

class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0152_auto_20160115_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitacion',
            name='institucion',
            field=models.CharField(verbose_name='Institución:', max_length=255, db_column='Institucion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='edicion',
            field=models.PositiveIntegerField(verbose_name='Número de la edición:', max_length=10, db_column='Edicion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='contenido',
            field=models.CharField(verbose_name='Contenido:', max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z- .,;]*$', 'Has introducido caracteres incorrectos.')], db_column='Contenido_Noticia'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='publicacion',
            field=models.DateField(verbose_name='Publicación:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='titular',
            field=models.CharField(verbose_name='Titular:', db_column='Titular', max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z- ]*$', 'Has introducido caracteres incorrectos.')], unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='obracientifica',
            name='descripcion',
            field=models.CharField(verbose_name='Descripción', max_length=255, db_column='Descripcion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='obracientifica',
            name='fecha_creacion',
            field=models.DateField(verbose_name='Fecha de creación'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='obracientifica',
            name='titulo',
            field=models.CharField(verbose_name='Título', max_length=128, db_column='Titulo', unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ponenciaevento',
            name='titulo',
            field=models.CharField(verbose_name='Título:', max_length=255, db_column='Titulo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='premio',
            name='titulo',
            field=models.CharField(verbose_name='Título:', max_length=255, db_column='Titulo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='anno_graduado',
            field=models.DateField(default=datetime.datetime(2016, 1, 3, 18, 23, 32, 31250, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='expediente',
            field=models.PositiveIntegerField(verbose_name='Expediente:', default=0, max_length=10, db_column='ID_Expediente'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyectoidi',
            name='titulo',
            field=models.CharField(verbose_name='Título:', max_length=255, db_column='Titulo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='numero',
            field=models.CharField(verbose_name='Número:', max_length=10, db_column='Numero'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='publicacion',
            field=models.CharField(verbose_name='Publicación:', max_length=100, db_column='Publicacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='volumen',
            field=models.PositiveIntegerField(verbose_name='Volúmen:', max_length=10, db_column='Volumen'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultadointroducido',
            name='institucion',
            field=models.CharField(verbose_name='Institución donde se introdujo:', max_length=255, db_column='Institucion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='aprobador_cargo_SAI',
            field=models.CharField(null=True, max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z- ]*$', 'Has introducido caracteres incorrectos.')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='area_solicitante',
            field=models.CharField(max_length=255, db_column='Area_solicitante', validators=[django.core.validators.RegexValidator('^[a-zA-Z- ]*$', 'Has introducido caracteres incorrectos.')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='codigo',
            field=models.CharField(verbose_name='Código:', max_length=255, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Has introducido caracteres incorrectos.')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='comentario_SAI_No_Aprobacion',
            field=models.CharField(null=True, verbose_name='Comentar la no aprobación:', max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z- .,;]*$', 'Has introducido caracteres incorrectos.')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='comentario_SAI_evaluacion',
            field=models.CharField(null=True, verbose_name='Comentar evaluación:', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='descripcion_SAI',
            field=models.CharField(verbose_name='Descripción:', max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z- .,;]*$', 'Has introducido caracteres incorrectos.')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='evaluacion_SAI',
            field=models.ForeignKey(null=True, verbose_name='Evaluación:', to='FileSample.EvaluacionSAI'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='responsable_ejecucion_SAI',
            field=models.ForeignKey(null=True, verbose_name='Responsable ejecución SAI:', to=settings.AUTH_USER_MODEL, related_name='Responsable Ejecucion SAI'),
            preserve_default=True,
        ),
    ]
