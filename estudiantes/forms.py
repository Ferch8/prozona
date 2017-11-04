from django import forms
from .models import Estudiante, Curso

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ('nombre', 'carne', 'fecha_nacimiento', 'cursos')

    def __init__ (self, *args, **kwargs):
        super(EstudianteForm, self).__init__(*args, **kwargs)
        self.fields["cursos"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["cursos"].help_text = "Ingrese los cursos a asignar al estudiante"
        self.fields["cursos"].queryset = Curso.objects.all()
