# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('carne', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('cursos', models.ManyToManyField(to='estudiantes.Curso', through='estudiantes.Asignacion')),
            ],
        ),
        migrations.AddField(
            model_name='asignacion',
            name='curso',
            field=models.ForeignKey(to='estudiantes.Curso'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='estudiante',
            field=models.ForeignKey(to='estudiantes.Estudiante'),
        ),
    ]
