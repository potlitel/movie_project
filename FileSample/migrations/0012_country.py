# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0011_continent_poblation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Item name: ')),
                ('poblation', models.CharField(max_length=128, verbose_name='Item poblation: ')),
                ('continent', models.ForeignKey(to='FileSample.Continent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
