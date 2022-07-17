# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0029_auto_20150406_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='caracter',
            field=models.CharField(db_column='Caracter', verbose_name='Caracter:', max_length=25),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='contenido',
            field=models.CharField(db_column='Contenido_Noticia', verbose_name='Contenido:', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='titular',
            field=models.CharField(db_column='Titular', verbose_name='Titular:', max_length=255, unique=True),
            preserve_default=True,
        ),
    ]
