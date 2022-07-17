# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0146_auto_20160115_0009'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaDocente',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Categorias Docentes',
                'verbose_name': 'Categoria Docente',
                'ordering': ['nombre'],
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
