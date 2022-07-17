# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0054_auto_20150628_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date_joined', models.DateField()),
                ('invite_reason', models.CharField(max_length=64)),
                ('proyectoIDi', models.ForeignKey(to='FileSample.ProyectoIDi')),
                ('publicacion', models.ForeignKey(to='FileSample.Publicacion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='proyectoidi',
            name='publicaciones',
            field=models.ManyToManyField(db_table='Publications_To_Projects', to='FileSample.Publicacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyectoidi',
            name='fichero',
            field=models.FileField(max_length=255, db_column='Direccion_Fichero_Asociado', upload_to='FileSampleApp/ProjectoIdi', verbose_name='Asociar fichero'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyectoidi',
            name='nivel',
            field=models.CharField(max_length=15, db_column='Nivel', verbose_name='Nivel:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyectoidi',
            name='propietario',
            field=models.CharField(max_length=128, db_column='Propietario', verbose_name='Propietario:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyectoidi',
            name='titulo',
            field=models.CharField(max_length=255, db_column='Titulo', verbose_name='Titulo:'),
            preserve_default=True,
        ),
    ]
