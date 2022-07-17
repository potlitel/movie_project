# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0132_auto_20160103_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalRecibirSAI',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nombre', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Total de personas a recibir SAI',
                'verbose_name_plural': 'Totales de personas a recibir SAI',
                'ordering': ['nombre'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TematicaSAI',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nombre', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Temática de SAI',
                'verbose_name_plural': 'Temáticas de SAI',
                'ordering': ['nombre'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TiempoSAI',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nombre', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Tiempo SAI',
                'verbose_name_plural': 'Tiempos SAI',
                'ordering': ['nombre'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='membresia',
            name='proyectoIDi',
            field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            preserve_default=True,
        ),
    ]
