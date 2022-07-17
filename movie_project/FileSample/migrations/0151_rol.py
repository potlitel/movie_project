# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0150_tituloacademico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'verbose_name': 'Rol',
                'ordering': ['nombre'],
                'verbose_name_plural': 'Roles',
            },
            bases=(models.Model,),
        ),
    ]
