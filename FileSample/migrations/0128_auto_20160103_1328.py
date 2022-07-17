# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FileSample', '0127_auto_20160103_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membresia',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('rol', models.CharField(max_length=64)),
                ('participantes', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('proyectoIDi', models.ForeignKey(to='FileSample.ProyectoiDi')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='membresia',
            unique_together=set([('participantes', 'proyectoIDi')]),
        ),
        migrations.AlterField(
            model_name='membership',
            name='proyectoIDi',
            field=models.ForeignKey(to='FileSample.ProyectoiDi'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyectoidi',
            name='participantes',
            field=models.ManyToManyField(through='FileSample.Membresia', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
