from django.db import models
from django.contrib import admin
# Create your models here.

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dpi = models.CharField(max_length=20)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=80)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return "%s %s" % (self.nombre, self.apellido)

class Aula(models.Model):
    nombre = models.CharField(max_length=50)
    encargado = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre  =   models.CharField(max_length=30)
    descripcion  =   models.CharField(max_length=100)
    fecha_creacion = models.DateField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)

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
