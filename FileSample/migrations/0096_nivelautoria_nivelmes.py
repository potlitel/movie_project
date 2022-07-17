# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0095_obracientifica_propietario'),
    ]

    operations = [
        migrations.CreateModel(
            name='NivelAutoria',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Niveles de Autoria',
                'verbose_name': 'Nivel de Autoria',
                'ordering': ['nombre'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NivelMES',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Niveles de MES',
                'verbose_name': 'Nivel de MES',
                'ordering': ['nombre'],
            },
            bases=(models.Model,),
        ),
    ]
