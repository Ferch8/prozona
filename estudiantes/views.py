from django.shortcuts import render,redirect, get_object_or_404
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
            return redirect('estudiante_list')
    else:
        formulario = EstudianteForm()
    return render(request, 'estudiantes/estudiante_nuevo.html', {'formulario': formulario})

def curso_nuevo(request):
    if request.method=="POST":
        formulario = CursoForm(request.POST)
        if formulario.is_valid():
            Curso = formulario.save(commit=False)
            Curso.save()
            return redirect('cursos_list')
    else:
        formulario = CursoForm()
    return render(request, 'estudiantes/curso_nuevo.html', {'formulario':formulario})

def profesor_nuevo(request):
    if request.method == "POST":
        formulario = ProfesorForm(request.POST)
        if formulario.is_valid():
            profesor = formulario.save(commit=False)
            profesor.save()
            return redirect('profesor_list')
    else:
        formulario = ProfesorForm()
    return render(request, 'estudiantes/profesor_nuevo.html', {'formulario': formulario})

def aula_nuevo(request):
    if request.method == "POST":
        formulario = AulaForm(request.POST)
        if formulario.is_valid():
            aula = formulario.save(commit=False)
            aula.save()
            return redirect('aula_list')
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
            return redirect('estudiante_list')
    else:
        formulario = EstudianteForm(instance=estudiante)
    return render(request, 'estudiantes/estudiante_editar.html', {'formulario': formulario})

def curso_editar(request,pk):
    curso = get_object_or_404(Curso,pk=pk)
    if request.method=="POST":
        formulario = CursoForm(request.POST,instance=curso)
        if formulario.is_valid():
            curso = formulario.save()
            return redirect('cursos_list')
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
            return redirect('profesor_list')
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
            return redirect('aula_list')
    else:
        formulario = AulaForm(instance=aula)
    return render(request, 'estudiantes/aula_editar.html', {'formulario': formulario})

def estudiante_list(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/estudiante_list.html', {'estudiantes': estudiantes})

def cursos_list(request):
    cursos = Curso.objects.all()
    return render(request, 'estudiantes/cursos_list.html', {'cursos': cursos})

def profesor_list(request):
    profesores = Profesor.objects.all()
    return render(request, 'estudiantes/profesores_list.html', {'profesores': profesores})

def aula_list(request):
    aulas = Aula.objects.all()
    return render(request, 'estudiantes/aula_list.html', {'aulas': aulas})

def estudiante_ver(request,pk):
    estudiante = get_object_or_404(Estudiante,pk=pk)
    return render(request, 'estudiantes/estudiante_ver.html', {'estudiante': estudiante})

def curso_ver(request,pk):
    curso = get_object_or_404(Curso,pk=pk)
    return render(request, 'estudiantes/curso_ver.html', {'curso': curso})

def profesor_ver(request,pk):
    profesor = get_object_or_404(Profesor,pk=pk)
    return render(request, 'estudiantes/profesor_ver.html', {'profesor': profesor})

def aula_ver(request,pk):
    aula = get_object_or_404(Aula,pk=pk)
    return render(request, 'estudiantes/aula_ver.html', {'aula': aula})

def estudiante_eliminar(request,pk):
    estudiante = get_object_or_404(Estudiante,pk=pk)
    estudiante.delete()
    return redirect('estudiante_list')

def curso_eliminar(request,pk):
    curso = get_object_or_404(Curso,pk=pk)
    curso.delete()
    return redirect('curso_list')

def profesor_eliminar(request,pk):
    profesor = get_object_or_404(Profesor,pk=pk)
    profesor.delete()
    return redirect('profesor_list')

def aula_eliminar(request,pk):
    aula = get_object_or_404(Aula,pk=pk)
    aula.delete()
    return redirect('aula_list')
