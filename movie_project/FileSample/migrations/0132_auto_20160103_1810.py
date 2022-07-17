# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0131_auto_20160103_1809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subtiposaisolicitado',
            old_name='area',
            new_name='tipo',
        ),
    ]
