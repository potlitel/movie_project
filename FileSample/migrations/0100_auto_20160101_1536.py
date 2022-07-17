# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0099_cienciaobra_tipoobra'),
    ]

    operations = [
        migrations.CreateModel(
            name='TamañoObra',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name': 'Tamaño de Obra',
                'verbose_name_plural': 'Tamaños de Obras',
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
