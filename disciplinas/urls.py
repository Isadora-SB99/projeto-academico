from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar-disciplina/', views.cadastrar_disciplina, name='cadastrar_disciplina'),
    path('disciplinas/', views.listar_disciplinas, name='listar_disciplinas'),
    path('listar_alunos__para_matricula/', views.listar_alunos_para_matricula, name='listar_alunos_para_matricula'),
    path('matricular/<int:aluno_id>/', views.matricular_aluno, name='matricular_aluno'),
    path('historico-matriculas/', views.historico_matriculas, name='historico_matriculas'),
]
