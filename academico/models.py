from stdimage.models import StdImageField
from django.db import models

GENERO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('NB', 'Não-binário'),
    ('O', 'Outro'),
]

ESTADO_CIVIL_CHOICES = [
    ('S', 'Solteiro'),
    ('C', 'Casado'),
    ('D', 'Divorciado'),
    ('V', 'Viúvo'),
]

ESCOLARIDADE_CHOICES = [
    ('fun', 'Fundamental'),
    ('med', 'Médio'),
    ('sup', 'Superior'),
    ('pos', 'Pós-graduação'),
    ('mes', 'Mestrado'),
    ('dou', 'Doutorado'),
]


class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if self.nome:
            self.nome = self.formatar_nome_curso(self.nome)
        super().save(*args, **kwargs)

    def formatar_nome_curso(self, nome):
        partes = nome.lower().split()
        minusculas = ['da', 'de', 'do', 'das', 'dos', 'e',
                      'em', 'a', 'o', 'as', 'os', 'para', 'com']

        return ' '.join([
            p if p in minusculas else p.capitalize()
            for p in partes
        ])



class Aluno(models.Model):
    nome = models.CharField("digite o nome: ", max_length=100)
    data_nascimento = models.DateField("informe a data de nascimento: ")
    cpf = models.CharField("digite o cpf: ", max_length=14, unique=True)
    genero = models.CharField("selecione o gênero: ", max_length=2, choices=GENERO_CHOICES)
    estado_civil = models.CharField("selecione o estado civil: ", max_length=30, choices=ESTADO_CIVIL_CHOICES)
    escolaridade = models.CharField("selecione o nível de escolaridade: ", max_length=50, choices=ESCOLARIDADE_CHOICES)
    curso = models.ForeignKey(Curso, on_delete=models.RESTRICT)
    ativo = models.BooleanField(default=True)
    foto = StdImageField(
        upload_to='fotos/alunos',
        variations={'thumb': (150, 150), 'medium': (300, 300)},
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if self.nome:
            self.nome = self.formatar_nome(self.nome)
        super().save(*args, **kwargs)

    def formatar_nome(self, nome):
        partes = nome.lower().split()
        minusculas = ['da', 'de', 'do', 'das', 'dos', 'e']

        return ' '.join([
            p if p in minusculas else p.capitalize()
            for p in partes
        ])

