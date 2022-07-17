# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0133_auto_20160103_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluacionSAI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Evaluaciones de SAI',
                'ordering': ['nombre'],
                'verbose_name': 'Evaluacion de SAI',
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
