# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FileSample', '0142_auto_20160110_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('department', models.CharField(max_length=100)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='perfil')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='saisaprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='SAISAProfile',
        ),
        migrations.AlterField(
            model_name='membresia',
            name='proyectoIDi',
            field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            preserve_default=True,
        ),
    ]
