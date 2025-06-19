from django.db import models
from academico.models import Aluno, Curso

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    vagas = models.PositiveIntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.RESTRICT, related_name='disciplinas')

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if self.nome:
            self.nome = self._formatar_nome(self.nome)
        super().save(*args, **kwargs)

    def _formatar_nome(self, nome):
        minusculas = ['da', 'de', 'do', 'das', 'dos', 'e', 'em', 'a', 'o', 'as', 'os', 'para', 'com', 'ao','à',]
        partes = nome.lower().split()
        return ' '.join([p if p in minusculas else p.capitalize() for p in partes])

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.RESTRICT)
    disciplinas = models.ManyToManyField(Disciplina)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.aluno.nome
