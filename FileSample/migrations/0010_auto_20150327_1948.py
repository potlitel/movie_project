# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0009_auto_20150327_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Item name: ')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='file',
            name='gender',
            field=models.CharField(max_length=20, verbose_name='Gender'),
            preserve_default=True,
        ),
    ]
