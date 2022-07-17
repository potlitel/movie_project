# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FileSample', '0162_auto_20160208_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacion',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='nivel_autoria',
        ),
        migrations.AddField(
            model_name='publicacion',
            name='autores',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, db_table='Publicacion_Autores', related_name='Publicacion_Autores'),
            preserve_default=True,
        ),
        # migrations.AlterField(
            # model_name='profile',
            # name='anno_graduado',
            # field=models.DateField(default=0),
            # preserve_default=True,
        # ),
    ]
