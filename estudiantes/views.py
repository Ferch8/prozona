from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import EstudianteForm, CursoForm, ProfesorForm, AulaForm
from estudiantes.models import Estudiante, Asignacion, Curso, Profesor, Aula
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
    return render(request, 'estudiantes/estudiante_nuevo.html', {'formulario': formulario})

def curso_nuevo(request):
    if request.method=="POST":
        formulario = CursoForm(request.POST)
        if formulario.is_valid():
            Curso = formulario.save(commit=False)
            Curso.save()
            messages.add_message(request, messages.SUCCESS, 'Curso Guardado Exitosamente')
    else:
        formulario = CursoForm()
    return render(request, 'estudiantes/curso_nuevo.html', {'formulario':formulario})

def profesor_nuevo(request):
    if request.method == "POST":
        formulario = ProfesorForm(request.POST)
        if formulario.is_valid():
            profesor = formulario.save(commit=False)
            profesor.save()
            messages.add_message(request, messages.SUCCESS, 'Profesor creado Exitosamente')
    else:
        formulario = ProfesorForm()
    return render(request, 'estudiantes/profesor_nuevo.html', {'formulario': formulario})

def aula_nuevo(request):
    if request.method == "POST":
        formulario = AulaForm(request.POST)
        if formulario.is_valid():
            aula = formulario.save(commit=False)
            aula.save()
            messages.add_message(request, messages.SUCCESS, 'Aula creado Exitosamente')
    else:
        formulario = AulaForm()
    return render(request, 'estudiantes/aula_nuevo.html', {'formulario': formulario})

def estudiante_editar(request, pk):
    estudiante = get_object_or_404(Estudiante,pk=pk)
    if request.method == "POST":
        formulario = EstudianteForm(request.POST, instance=estudiante)
        if formulario.is_valid():
            estudiante = Estudiante.objects.create(nombre=formulario.cleaned_data['nombre'], carne=formulario.cleaned_data['carne'], fecha_nacimiento = formulario.cleaned_data['fecha_nacimiento'])
            for curso_id in request.POST.getlist('cursos'):
                asignacion = Asignacion(curso_id=curso_id, estudiante_id = estudiante.id)
                asignacion.save()
            messages.add_message(request, messages.SUCCESS, 'Estudiante Guardado Exitosamente')
    else:
        formulario = EstudianteForm(instance=estudiante)
    return render(request, 'estudiantes/estudiante_editar.html', {'formulario': formulario})

def curso_editar(request,pk):
    curso = get_object_or_404(Curso,pk=pk)
    if request.method=="POST":
        formulario = CursoForm(request.POST,instance=curso)
        if formulario.is_valid():
            curso = formulario.save()
            messages.add_message(request, messages.SUCCESS, 'Curso modificado Exitosamente')
    else:
        formulario=CursoForm(instance=curso)
    return render(request, 'estudiantes/curso_editar.html', {'formulario':formulario})

def profesor_editar(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == "POST":
        formulario = ProfesorForm(request.POST, instance=profesor)
        if formulario.is_valid():
            profesor = formulario.save(commit=False)
            profesor.save()
            messages.add_message(request, messages.SUCCESS, 'Profesor modificado Exitosamente')
    else:
        formulario = ProfesorForm(instance=profesor)
    return render(request, 'estudiantes/profesor_editar.html', {'formulario': formulario})

def aula_editar(request, pk):
    aula = get_object_or_404(Aula, pk=pk)
    if request.method == "POST":
        formulario = AulaForm(request.POST, instance=aula)
        if formulario.is_valid():
            aula = formulario.save(commit=False)
            aula.save()
            messages.add_message(request, messages.SUCCESS, 'Aula modificado Exitosamente')
    else:
        formulario = AulaForm(instance=aula)
    return render(request, 'estudiantes/aula_editar.html', {'formulario': formulario})

def cursos_list(request):
    cursos = Curso.objects.all()
    return render(request, 'estudiantes/cursos_list.html', {'cursos': cursos})
