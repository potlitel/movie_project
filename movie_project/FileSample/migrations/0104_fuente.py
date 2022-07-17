# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0103_auto_20160101_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fuente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name': 'Fuente de Empleo de estudiantes',
                'verbose_name_plural': 'Fuentes de Empleo de estudiantes',
            },
            bases=(models.Model,),
        ),
    ]
