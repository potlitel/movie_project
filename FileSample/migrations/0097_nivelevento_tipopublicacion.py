# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0096_nivelautoria_nivelmes'),
    ]

    operations = [
        migrations.CreateModel(
            name='NivelEvento',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Niveles de Evento',
                'verbose_name': 'Nivel de Evento',
                'ordering': ['nombre'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoPublicacion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Tipos de publicación',
                'verbose_name': 'Tipo de publicación',
                'ordering': ['nombre'],
            },
            bases=(models.Model,),
        ),
    ]
