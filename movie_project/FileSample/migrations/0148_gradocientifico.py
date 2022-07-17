# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0147_auto_20160115_0013'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradoCientifico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name': 'Grado Cientifico',
                'ordering': ['nombre'],
                'verbose_name_plural': 'Grados Cientificos',
            },
            bases=(models.Model,),
        ),
    ]
