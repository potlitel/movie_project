# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('FileSample', '0033_auto_20150407_0658'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Paises',
                'verbose_name': 'Pais',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='empleoestudiantes',
            name='propietario',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], max_length=128, verbose_name='Propietario:', db_column='Propietario'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='contenido',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], max_length=255, verbose_name='Contenido:', db_column='Contenido_Noticia'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='propietario',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], max_length=128, verbose_name='Propietario:', db_column='Propietario'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='titular',
            field=models.CharField(unique=True, max_length=255, verbose_name='Titular:', validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], db_column='Titular'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patente',
            name='comentario',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], max_length=255, verbose_name='Comentario:', db_column='Comentario'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patente',
            name='nombre_obra',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], max_length=255, verbose_name='Nombre de la obra:', db_column='Nombre_Obra'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patente',
            name='propietario',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], max_length=128, verbose_name='Propietario:', db_column='Propietario'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='premio',
            name='autor',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], max_length=255, verbose_name='Autor:', db_column='Autor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='premio',
            name='propietario',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], max_length=128, verbose_name='Propietario:', db_column='Propietario'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='premio',
            name='titulo',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], max_length=255, verbose_name='Titulo:', db_column='Titulo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultadointroducido',
            name='comentario',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], max_length=255, verbose_name='Comentario:', db_column='Comentario'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultadointroducido',
            name='institucion',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], max_length=255, verbose_name='Institucion donde se introdujo:', db_column='Institucion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultadointroducido',
            name='nombre_obra',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], max_length=255, verbose_name='Nombre de la obra:', db_column='Nombre_Obra'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultadointroducido',
            name='propietario',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Este campo contiene caracteres no permitidos.')], max_length=128, verbose_name='Propietario:', db_column='Propietario'),
            preserve_default=True,
        ),
    ]
