# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FileSample', '0090_auto_20151229_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='obracientifica',
            name='propietario',
            field=models.ForeignKey(related_name='propietarioObraCientifica', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
