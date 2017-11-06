from django import forms
from .models import Estudiante, Curso , Profesor, Aula

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ('nombre', 'carne', 'fecha_nacimiento', 'cursos')

    def __init__ (self, *args, **kwargs):
        super(EstudianteForm, self).__init__(*args, **kwargs)
        self.fields["cursos"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["cursos"].help_text = "Ingrese los cursos a asignar al estudiante"
        self.fields["cursos"].queryset = Curso.objects.all()

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields =('nombre','descripcion','fecha_creacion','profesor','aula',)
        widgets = {
            'profesor':forms.Select,
            'aula':forms.Select,
}

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ('nombre', 'apellido','dpi','edad','direccion','email',)

class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = ('nombre', 'encargado',)
