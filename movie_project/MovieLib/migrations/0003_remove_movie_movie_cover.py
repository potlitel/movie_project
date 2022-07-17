# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MovieLib', '0002_movie_movie_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='movie_cover',
        ),
    ]
