# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0144_auto_20160112_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Municipios',
                'verbose_name': 'Municipio',
                'ordering': ['nombre'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Provincias',
                'verbose_name': 'Provincia',
                'ordering': ['nombre'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='municipio',
            name='provincia',
            field=models.ForeignKey(to='FileSample.Provincia'),
            preserve_default=True,
        ),
    ]
