# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0171_auto_20160225_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleoestudiantes',
            name='fuente',
        ),
        migrations.RemoveField(
            model_name='empleoestudiantes',
            name='nombre_fuente',
        ),
        migrations.RemoveField(
            model_name='empleoestudiantes',
            name='nombre_obra',
        ),
        migrations.AddField(
            model_name='empleoestudiantes',
            name='obracientifica',
            field=models.ForeignKey(null=True, verbose_name='Obra Científica a emplear:', to='FileSample.ObraCientifica'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='empleoestudiantes',
            name='ponenciaevento',
            field=models.ForeignKey(null=True, verbose_name='Ponencia a emplear:', to='FileSample.PonenciaEvento'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='empleoestudiantes',
            name='proyecto',
            field=models.ForeignKey(null=True, verbose_name='Proyecto a emplear:', to='FileSample.ProyectoiDi'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='empleoestudiantes',
            name='publicacion',
            field=models.ForeignKey(null=True, verbose_name='Publicacion a emplear:', to='FileSample.Publicacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='capacitacion',
            name='institucion',
            field=models.CharField(verbose_name='Institución:', validators=[django.core.validators.RegexValidator('^[a-zA-Z-  .,;]*$', 'Has introducido caracteres incorrectos.')], max_length=255, db_column='Institucion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='capacitacion',
            name='nombre',
            field=models.CharField(verbose_name='Nombre:', validators=[django.core.validators.RegexValidator('^[a-zA-Z-  .,;]*$', 'Has introducido caracteres incorrectos.')], max_length=255, db_column='Nombre'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='nombre',
            field=models.CharField(verbose_name='Nombre:', validators=[django.core.validators.RegexValidator('^[a-zA-Z-  .,;]*$', 'Has introducido caracteres incorrectos.')], max_length=255, db_column='Nombre'),
            preserve_default=True,
        ),
        # migrations.AlterField(
            # model_name='membresia',
            # name='proyectoIDi',
            # field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            # preserve_default=True,
        # ),
        migrations.AlterField(
            model_name='noticia',
            name='titular',
            field=models.CharField(verbose_name='Titular:', validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z- .,;]*$', 'Has introducido caracteres incorrectos.')], max_length=255, unique=True, db_column='Titular'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='obracientifica',
            name='titulo',
            field=models.CharField(verbose_name='Título', validators=[django.core.validators.RegexValidator('^[a-zA-Z-  .,;]*$', 'Has introducido caracteres incorrectos.')], max_length=128, unique=True, db_column='Titulo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ponenciaevento',
            name='titulo',
            field=models.CharField(verbose_name='Título:', validators=[django.core.validators.RegexValidator('^[a-zA-Z-  .,;]*$', 'Has introducido caracteres incorrectos.')], max_length=255, db_column='Titulo'),
            preserve_default=True,
        ),
        # migrations.AlterField(
            # model_name='premio',
            # name='proyecto',
            # field=models.ForeignKey(null=True, verbose_name='Proyecto a premiar:', to='FileSample.ProyectoiDi'),
            # preserve_default=True,
        # ),
        migrations.AlterField(
            model_name='premio',
            name='titulo',
            field=models.CharField(verbose_name='Título:', validators=[django.core.validators.RegexValidator('^[a-zA-Z-  .,;]*$', 'Has introducido caracteres incorrectos.')], max_length=255, db_column='Titulo'),
            preserve_default=True,
        ),
        # migrations.AlterField(
            # model_name='profile',
            # name='anno_graduado',
            # field=models.DateField(default=0),
            # preserve_default=True,
        # ),
        migrations.AlterField(
            model_name='publicacion',
            name='editorial',
            field=models.CharField(verbose_name='Editorial:', validators=[django.core.validators.RegexValidator('^[a-zA-Z-  .,;]*$', 'Has introducido caracteres incorrectos.')], max_length=50, db_column='Editorial'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='publicacion',
            field=models.CharField(verbose_name='Publicación:', validators=[django.core.validators.RegexValidator('^[a-zA-Z-  .,;]*$', 'Has introducido caracteres incorrectos.')], max_length=100, db_column='Publicacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='titulo',
            field=models.CharField(verbose_name='Titulo:', validators=[django.core.validators.RegexValidator('^[a-zA-Z-  .,;]*$', 'Has introducido caracteres incorrectos.')], max_length=255, db_column='Titulo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultadointroducido',
            name='institucion',
            field=models.CharField(verbose_name='Institución donde se introdujo:', validators=[django.core.validators.RegexValidator('^[a-zA-Z-  .,;]*$', 'Has introducido caracteres incorrectos.')], max_length=255, db_column='Institucion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='aprobador_cargo_SAI',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z-  .,;]*$', 'Has introducido caracteres incorrectos.')], null=True, max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sai',
            name='area_solicitante',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z-  .,;]*$', 'Has introducido caracteres incorrectos.')], max_length=255, db_column='Area_solicitante'),
            preserve_default=True,
        ),
    ]
