from django.db import models
from django.contrib import admin
# Create your models here.
class Curso(models.Model):
    nombre  =   models.CharField(max_length=30)
    descripcion  =   models.CharField(max_length=100)
    fecha_creacion = models.DateField()
    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre    = models.CharField(max_length=60)
    carne      = models.IntegerField()
    fecha_nacimiento = models.DateField()
    cursos   = models.ManyToManyField(Curso, through='Asignacion')
    def __str__(self):
        return self.nombre

class Asignacion (models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

class AsignacionInLine(admin.TabularInline):
    model = Asignacion
    extra = 1

class CursoAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)

class EstudianteAdmin (admin.ModelAdmin):
    inlines = (AsignacionInLine,)
