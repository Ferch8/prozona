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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('encargado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateField()),
                ('aula', models.ForeignKey(null=True, to='estudiantes.Aula', blank=True)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=60)),
                ('carne', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('cursos', models.ManyToManyField(through='estudiantes.Asignacion', to='estudiantes.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('dpi', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('direccion', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='profesor',
            field=models.ForeignKey(to='estudiantes.Profesor'),
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
