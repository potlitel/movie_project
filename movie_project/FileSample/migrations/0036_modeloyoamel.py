# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0035_auto_20150409_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModeloYoamel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('href', models.CharField(max_length=128, verbose_name='href (Relacionado con):', db_column='href', validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')])),
                ('data_largesrc', models.CharField(max_length=255, verbose_name='data_largesrc (Imagen grande):', db_column='data_largesrc')),
                ('data_title', models.CharField(max_length=255, verbose_name='data_title (Titulo):', db_column='data_title', validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')])),
                ('data_description', models.CharField(max_length=20, verbose_name='data_description (Descripción):', db_column='data_description')),
                ('img', models.CharField(max_length=255, verbose_name='Img (Imagen pequeña)', db_column='Img')),
            ],
            options={
                'verbose_name': 'Modelo Yoamel',
                'verbose_name_plural': 'Modelos Yoamel',
            },
            bases=(models.Model,),
        ),
    ]
