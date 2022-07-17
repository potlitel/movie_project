# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0149_auto_20160115_0018'),
    ]

    operations = [
        migrations.CreateModel(
            name='TituloAcademico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name': 'Titulo Academico',
                'verbose_name_plural': 'Titulos Academicos',
                'ordering': ['nombre'],
            },
            bases=(models.Model,),
        ),
    ]
