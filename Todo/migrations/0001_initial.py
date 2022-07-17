# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=40)),
                ('priority', models.PositiveSmallIntegerField(choices=[(0, 'Low'), (5, 'Normal'), (10, 'High'), (15, 'Urgent')], default=5)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('due_on', models.DateField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['due_on'],
                'permissions': (('view_todo', 'Can view todo'),),
            },
            bases=(models.Model,),
        ),
    ]
