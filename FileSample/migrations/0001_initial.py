# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('item', models.CharField(verbose_name='Item name: ', max_length=128)),
                ('image', models.ImageField(verbose_name='Image: ', upload_to='FileSample/')),
                ('File', models.FileField(verbose_name='File: ', upload_to='FileSample/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
