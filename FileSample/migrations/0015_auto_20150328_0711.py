# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0014_file_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='continent',
            old_name='name',
            new_name='continent_name',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='name',
            new_name='country_name',
        ),
        migrations.AlterField(
            model_name='file',
            name='continent',
            field=models.CharField(verbose_name='Continent', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='file',
            name='country',
            field=models.CharField(verbose_name='Country', max_length=20),
            preserve_default=True,
        ),
    ]
