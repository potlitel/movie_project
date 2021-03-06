# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0092_auto_20151229_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obracientifica',
            name='propietario',
            field=models.ForeignKey(related_name='propietario_ObraCientifica', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
