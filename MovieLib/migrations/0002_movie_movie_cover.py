# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MovieLib', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_cover',
            field=models.ImageField(default='path', upload_to='stuff_images/'),
            preserve_default=False,
        ),
    ]
