# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0098_auto_20160101_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='CienciaObra',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name': 'Ciencia de Obra',
                'verbose_name_plural': 'Ciencias de Obras',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoObra',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name': 'Tipo de Obra',
                'verbose_name_plural': 'Tipos de Obras',
            },
            bases=(models.Model,),
        ),
    ]
