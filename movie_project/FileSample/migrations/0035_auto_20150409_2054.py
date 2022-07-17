# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0034_auto_20150408_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(unique=True, max_length=128)),
                ('pais', models.ForeignKey(to='FileSample.Pais')),
            ],
            options={
                'verbose_name_plural': 'Ciudades',
                'verbose_name': 'Ciudad',
                'ordering': ['nombre'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries', 'verbose_name': 'Country'},
        ),
        migrations.AlterModelOptions(
            name='pais',
            options={'verbose_name_plural': 'Paises', 'verbose_name': 'Pais', 'ordering': ['nombre']},
        ),
    ]
