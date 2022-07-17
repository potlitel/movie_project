# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0104_fuente'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaracterNoticia',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name': 'Caracter de noticia',
                'verbose_name_plural': 'Caracteres de noticias',
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
