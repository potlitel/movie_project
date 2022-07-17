# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0100_auto_20160101_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaracterPremio',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Caracteres de Premios',
                'ordering': ['nombre'],
                'verbose_name': 'Caracter de Premio',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LugarPremio',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Lugares de Premios',
                'ordering': ['nombre'],
                'verbose_name': 'Lugar de Premio',
            },
            bases=(models.Model,),
        ),
        # migrations.AlterField(
            # model_name='membership',
            # name='proyectoIDi',
            # field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            # preserve_default=True,
        # ),
    ]
