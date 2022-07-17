# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0122_auto_20160102_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=150, unique=True)),
                ('descripcion', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Area',
                'ordering': ['nombre'],
                'verbose_name_plural': 'Areas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=150, unique=True)),
                ('descripcion', models.CharField(max_length=255)),
                ('area', models.ForeignKey(to='FileSample.Area')),
            ],
            options={
                'verbose_name': 'Grupo',
                'ordering': ['nombre'],
                'verbose_name_plural': 'Grupos',
            },
            bases=(models.Model,),
        ),
    ]
