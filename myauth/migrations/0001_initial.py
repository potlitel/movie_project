# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import re
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters', max_length=30, verbose_name='username', unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'Enter a valid username.', 'invalid')])),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name', null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name', null=True)),
                ('email', models.EmailField(max_length=255, verbose_name='email address', db_index=True, unique=True)),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', verbose_name='staff status', default=False)),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active', default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('receive_newsletter', models.BooleanField(default=False, verbose_name='receive newsletter')),
                ('groups', models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', related_name='user_set', related_query_name='user', blank=True, verbose_name='groups', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', blank=True, verbose_name='user permissions', to='auth.Permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
    ]
