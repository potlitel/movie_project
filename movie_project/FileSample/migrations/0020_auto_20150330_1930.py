# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0019_auto_20150329_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(db_column='Nombre', verbose_name='Nombre:', max_length=255)),
                ('edicion', models.CharField(db_column='Edicion', verbose_name='Numero de la edicion:', max_length=10)),
                ('nivel', models.CharField(db_column='Nivel', verbose_name='Nivel:', max_length=20)),
                ('pais', models.CharField(db_column='Pais', verbose_name='Pais:', max_length=50)),
                ('ciudad', models.CharField(db_column='Ciudad', verbose_name='Ciudad:', max_length=50)),
                ('tipo_publicacion', models.IntegerField(db_column='Tipo_Publicacion', verbose_name='Tipo de publicacion:', max_length=25)),
                ('issn', models.CharField(db_column='ISSN', verbose_name='ISSN:', max_length=20)),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='anno',
            field=models.IntegerField(db_column='Anno', verbose_name='Año:', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='aprobacion',
            field=models.BooleanField(default='False', db_column='Aprobacion', verbose_name='Aprobacion:', max_length=1000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='autor',
            field=models.CharField(db_column='Autor', verbose_name='Autor:', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='ciudad',
            field=models.CharField(db_column='Ciudad', verbose_name='Ciudad:', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='editorial',
            field=models.CharField(db_column='Editorial', verbose_name='Editorial:', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='nivel_autoria',
            field=models.CharField(db_column='Nivel_Autoria', verbose_name='Nivel de Autoria:', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='nivel_mes',
            field=models.IntegerField(db_column='Nivel_MES', verbose_name='Nivel MES:', max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='numero',
            field=models.CharField(db_column='Numero', verbose_name='Numero:', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='pais',
            field=models.CharField(db_column='Pais', verbose_name='Pais:', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='propietario',
            field=models.CharField(db_column='Propietario', verbose_name='Propietario:', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='publicacion',
            field=models.CharField(db_column='Publicacion', verbose_name='Publicacion:', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='titulo',
            field=models.CharField(db_column='Titulo', verbose_name='Titulo:', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='volumen',
            field=models.IntegerField(db_column='Volumen', verbose_name='Volumen:', max_length=10),
            preserve_default=True,
        ),
    ]
