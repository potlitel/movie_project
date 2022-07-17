# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FileSample', '0134_auto_20160103_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='SAI',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('area_solicitante', models.CharField(max_length=255)),
                ('fecha', models.DateField()),
                ('codigo', models.CharField(max_length=255)),
                ('nombre_solicitante', models.CharField(max_length=255)),
                ('cargo_solicitante', models.CharField(max_length=255)),
                ('solapin_solicitante', models.CharField(max_length=255)),
                ('telefono_solicitante', models.PositiveIntegerField(max_length=255)),
                ('email_solicitante', models.EmailField(max_length=255)),
                ('descripcion_SAI', models.CharField(max_length=255)),
                ('aprobacion', models.BooleanField(default='False', verbose_name='Aprobacion:', db_column='Aprobacion', max_length=1000)),
                ('aprobador_cargo_SAI', models.CharField(max_length=255)),
                ('responsable_ejecucion_SAI', models.CharField(max_length=255)),
                ('comentario_SAI_No_Aprobacion', models.CharField(max_length=255)),
                ('comentario_SAI_evaluacion', models.CharField(max_length=255)),
                ('aprobador_SAI', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='Aprobador SAI')),
                ('evaluacion_SAI', models.ForeignKey(to='FileSample.EvaluacionSAI')),
                ('personal_SAI', models.ForeignKey(to='FileSample.PersonalRecibirSAI')),
                ('solicitante', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('subtipo_SAI', models.ForeignKey(to='FileSample.SubTipoSAISolicitado')),
                ('tematica_SAI', models.ForeignKey(to='FileSample.TematicaSAI')),
                ('tiempo_SAI', models.ForeignKey(to='FileSample.TiempoSAI')),
                ('tipo_SAI', models.ForeignKey(to='FileSample.TipoSAISolicitado')),
            ],
            options={
                'ordering': ['area_solicitante'],
                'verbose_name': 'SAI',
                'verbose_name_plural': 'SAIs',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='membership',
            name='proyectoIDi',
            field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membresia',
            name='proyectoIDi',
            field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            preserve_default=True,
        ),
    ]
