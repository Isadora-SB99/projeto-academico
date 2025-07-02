from django.shortcuts import render
from .models import Aluno, Curso
from .forms import CursoForm, AlunoForm
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import RestrictedError
from django.contrib.auth.decorators import login_required

ORDENACAO_ALUNOS_LOOKUP = {
    'curso': 'curso__nome',
    'nome': 'nome',
    'genero': 'genero',
    'escolaridade': 'escolaridade',
    'estado_civil': 'estado_civil',
    'data_nascimento': 'data_nascimento'
}

@login_required
def index(request):
    return render(request, 'academico/index.html')

@login_required
def alunos(request):
    query = request.GET.get('busca', '')
    if query:
        alunos = Aluno.objects.filter(ativo=True, nome__icontains=query)
    else:
        alunos = Aluno.objects.filter(ativo=True)
    dados = {
        'alunos': alunos,
        'ativos': True,
        'query': query,
    }
    return render(request, 'academico/lista_alunos.html', dados)


def cursos(request):
    cursos = Curso.objects.all()
    dados = {
        'cursos': cursos,
    }
    return render(request, 'academico/lista_cursos.html', dados)

@login_required
def cadastrar_aluno(request):

    if request.method == 'POST':
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('alunos')
    else:
        form = AlunoForm()
        dados = {
            'form': form,
        }
    return render(request, 'academico/cadastrar_aluno.html', dados)

@login_required
def cadastrar_curso(request):

    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CursoForm()
        dados = {
            'form': form,
        }
    return render(request, 'academico/cadastrar_curso.html', dados)

@login_required
def editar_aluno(request, id):
    try:
        aluno = Aluno.objects.get(id=id)
    except:
        return redirect('alunos')

    if request.method == 'POST':
        form = AlunoForm(request.POST, request.FILES, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('alunos')

    form = AlunoForm(instance=aluno)

    dados = {
        'form': form,
        'aluno': aluno,
    }

    return render(request, 'academico/editar_aluno.html', dados)

@login_required
def editar_curso(request, id):
    try:
        curso = Curso.objects.get(id=id)
    except:
        return redirect('cursos')

    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos')

    form = CursoForm(instance=curso)

    dados = {
        'form': form,
        'curso': curso,
    }

    return render(request, 'academico/editar_curso.html', dados)

@login_required
def excluir_aluno(request, id):
    try:
        aluno = Aluno.objects.get(id=id)
        aluno.ativo = False
        aluno.save()
        messages.success(request, "Aluno excluído com sucesso.")
    except Aluno.DoesNotExist:
        messages.error(request, "Aluno não encontrado.")

    return redirect('alunos')

@login_required
def excluir_curso(request, id):
    try:
        curso = Curso.objects.get(id=id)
        curso.delete()
        messages.success(request, "Curso excluído com sucesso.")
    except RestrictedError:
        messages.error(
            request, "Não é possível deletar o curso pois há alunos vinculados.")
    except Curso.DoesNotExist:
        messages.error(request, "Curso não encontrado.")

    return redirect('cursos')

@login_required
def alunos_inativos(request):
    query = request.GET.get('busca', '')
    if query:
        alunos = Aluno.objects.filter(ativo=False, nome__icontains=query)
    else:
        alunos = Aluno.objects.filter(ativo=False)

    dados = {
        'alunos': alunos,
        'ativos': False,
        'query': query
    }
    return render(request, 'academico/lista_alunos.html', dados)

@login_required
def ativar_aluno(request, id):
    try:
        aluno = Aluno.objects.get(id=id)
    except Aluno.DoesNotExist:
        messages.error(request, "Aluno não encontrado.")
        return redirect('alunos_inativos')

    if aluno.ativo == False:
        aluno.ativo = True
        aluno.save()
        messages.success(request, "Aluno reativado com sucesso.")

    else:
        messages.info(request, "O aluno já está ativo.")

    return redirect('alunos_inativos')

@login_required
def ordenar_alunos(request, campo):
    campo_ordenacao = ORDENACAO_ALUNOS_LOOKUP.get(campo)
    busca = request.GET.get('busca', '')
    alunos = Aluno.objects.filter(ativo=True)

    if busca:
        alunos = alunos.filter(nome__icontains=busca)

    alunos = alunos.order_by(campo_ordenacao)
    dados = {
        'alunos': alunos,
        'ativos': True,
        'query': busca,
    }
    return render(request, 'academico/lista_alunos.html', dados)

@login_required
def ordenar_alunos_inativos(request, campo):
    campo_ordenacao = ORDENACAO_ALUNOS_LOOKUP.get(campo)
    busca = request.GET.get('busca', '')
    alunos = Aluno.objects.filter(ativo=False)

    if busca:
        alunos = Aluno.objects.filter(nome__icontains=busca)

    alunos = alunos.order_by(campo_ordenacao)
    dados = {
        'alunos': alunos,
        'ativos': False,
        'query': busca,
    }
    return render(request, 'academico/lista_alunos.html', dados)

@login_required
def detalhes_aluno(request, aluno_id):
    try:
        aluno = Aluno.objects.get(id=aluno_id)
    except Aluno.DoesNotExist:
        messages.error(request, "Aluno não encontrado.")
        return redirect('alunos')
    
    dados = {
        'aluno': aluno,
    }

    return render(request, 'academico/detalhes_aluno.html', dados)
