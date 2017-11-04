from django.contrib import admin
from estudiantes.models import Curso, CursoAdmin, Estudiante, EstudianteAdmin
# Register your models here.
admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
