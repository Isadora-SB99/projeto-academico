from django import forms
from .models import Curso, Aluno


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome']


class AlunoForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Aluno
        fields = ['foto', 'nome', 'data_nascimento', 'cpf', 'genero', 'estado_civil', 'escolaridade', 'curso']
