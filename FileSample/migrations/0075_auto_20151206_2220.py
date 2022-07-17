# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0074_auto_20151004_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='ciudad',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_model_field='nombre', chained_field='pais', to='FileSample.Ciudad'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='pais',
            field=models.ForeignKey(to='FileSample.Pais'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together=set([('publicacion', 'proyectoIDi')]),
        ),
    ]
