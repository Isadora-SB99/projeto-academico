from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alunos/', views.alunos, name='alunos'),
    path('cadastrar_aluno/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('cadastrar_curso/', views.cadastrar_curso, name='cadastrar_curso'),
]
