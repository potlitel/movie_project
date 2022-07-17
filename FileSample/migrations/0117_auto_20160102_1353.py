# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0116_auto_20160102_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='caracter',
            field=models.ForeignKey(to='FileSample.CaracterNoticia'),
            preserve_default=True,
        ),
    ]
