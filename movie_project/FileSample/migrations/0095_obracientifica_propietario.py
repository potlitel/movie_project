# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FileSample', '0094_remove_obracientifica_propietario'),
    ]

    operations = [
        migrations.AddField(
            model_name='obracientifica',
            name='propietario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='propietario_ObraCientifica', default=1),
            preserve_default=False,
        ),
    ]
