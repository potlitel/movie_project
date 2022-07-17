# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0020_auto_20150330_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='edicion',
            field=models.IntegerField(verbose_name='Numero de la edicion:', max_length=10, db_column='Edicion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='tipo_publicacion',
            field=models.CharField(verbose_name='Tipo de publicacion:', max_length=25, db_column='Tipo_Publicacion'),
            preserve_default=True,
        ),
    ]
