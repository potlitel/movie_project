# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FileSample', '0088_auto_20151222_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObraCientifica',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('titulo', models.CharField(max_length=128, unique=True, db_column='Titulo')),
                ('fecha_creacion', models.DateField()),
                ('descripcion', models.CharField(max_length=255, db_column='Descripcion')),
                ('tamanno', models.CharField(max_length=15, db_column='Tamanno_Obra')),
                ('autores', models.ManyToManyField(db_table='ObraCientifica_Autores', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Obras cientificas',
                'verbose_name': 'Obra cientifica',
                'ordering': ['titulo'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoObraCientifica',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Tipos de obras cientificas',
                'verbose_name': 'Tipo de obra cientifica',
                'ordering': ['nombre'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='obracientifica',
            name='tipo_obra',
            field=models.ForeignKey(to='FileSample.TipoObraCientifica'),
            preserve_default=True,
        ),
    ]
