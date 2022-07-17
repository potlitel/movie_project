# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0123_area_grupo'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineaCientificaProyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name': 'Linea Cientifica de Proyecto',
                'verbose_name_plural': 'Lineas Cientificas de Proyectos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NivelProyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name': 'Nivel de Proyecto',
                'verbose_name_plural': 'Niveles de Proyectos',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='membership',
            name='proyectoIDi',
            field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            preserve_default=True,
        ),
    ]
