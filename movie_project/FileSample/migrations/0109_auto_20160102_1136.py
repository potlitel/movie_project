# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0108_auto_20160102_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitacion',
            name='modalidad',
            field=models.ForeignKey(to='FileSample.ModalidadCapacitacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='capacitacion',
            name='rol',
            field=models.ForeignKey(to='FileSample.RolCapacitación'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='capacitacion',
            name='tipo',
            field=models.ForeignKey(to='FileSample.TipoCapacitacion'),
            preserve_default=True,
        ),
    ]
