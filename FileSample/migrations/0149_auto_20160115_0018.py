# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0148_gradocientifico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name': 'Sexo',
                'verbose_name_plural': 'Sexos',
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
