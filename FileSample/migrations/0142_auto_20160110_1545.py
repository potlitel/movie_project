# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0141_auto_20160110_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saisaprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='perfil'),
            preserve_default=True,
        ),
    ]
