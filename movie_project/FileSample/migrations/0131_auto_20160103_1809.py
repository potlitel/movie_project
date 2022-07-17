# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0130_auto_20160103_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubTipoSAISolicitado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Sub Tipo de SAI',
                'verbose_name_plural': 'Sub Tipos de SAI',
                'ordering': ['nombre'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoSAISolicitado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Tipo de SAI',
                'verbose_name_plural': 'Tipos de SAI',
                'ordering': ['nombre'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='subtiposaisolicitado',
            name='area',
            field=models.ForeignKey(to='FileSample.TipoSAISolicitado'),
            preserve_default=True,
        ),
    ]
