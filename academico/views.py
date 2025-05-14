from django.shortcuts import render
from .models import Aluno, Curso
from .forms import CursoForm, AlunoForm

# Create your views here.

def index(request):
    return render(request, 'academico/index.html')

def alunos(request):
    alunos = Aluno.objects.all()
    dados = {
        'alunos': alunos,
    }
    return render(request, 'academico/lista_alunos.html', dados)

def cadastrar_aluno(request):
    form = AlunoForm() #form vai receber um formulário AlunoForm vazio que criamos no forms.py
    dados = {
        'form': form,
    }
    return render(request, 'academico/cadastrar_aluno.html', dados)   

def cadastrar_curso(request):
    form = CursoForm() #form vai receber um formulário CursoForm vazio que criamos no forms.py
    dados = {
        'form': form,
    }
    return render(request, 'academico/cadastrar_curso.html', dados)
