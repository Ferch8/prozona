from django.shortcuts import render
from django.contrib import messages
from .forms import EstudianteForm
from estudiantes.models import Estudiante, Asignacion
# Create your views here.
def estudiante_nuevo(request):
    if request.method == "POST":
        formulario = EstudianteForm(request.POST)
        if formulario.is_valid():
            estudiante = Estudiante.objects.create(nombre=formulario.cleaned_data['nombre'], carne=formulario.cleaned_data['carne'], fecha_nacimiento = formulario.cleaned_data['fecha_nacimiento'])
            for curso_id in request.POST.getlist('cursos'):
                asignacion = Asignacion(curso_id=curso_id, estudiante_id = estudiante.id)
                asignacion.save()
            messages.add_message(request, messages.SUCCESS, 'Estudiante Guardado Exitosamente')
    else:
        formulario = EstudianteForm()
    return render(request, 'estudiantes/estudiante_editar.html', {'formulario': formulario})
