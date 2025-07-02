from django.test import TestCase
from .models import Curso


class CursoModelTest(TestCase):

    def test_criacao_curso(self):
        curso = Curso.objects.create(nome="Matemática")
        self.assertEqual(Curso.objects.count(), 1)
        self.assertEqual(curso.nome, "Matemática")

        curso = Curso.objects.create(nome="português")
        self.assertEqual(Curso.objects.count(), 2)
        self.assertEqual(curso.nome, "Português")

        curso = Curso.objects.create(nome="sistemas de InForMaÇãO")
        self.assertEqual(Curso.objects.count(), 3)
        self.assertEqual(curso.nome, "Sistemas de Informação")

        curso = Curso.objects.create(nome="DIREITO")
        self.assertEqual(Curso.objects.count(), 4)
        self.assertEqual(curso.nome, "Direito")

        curso = Curso.objects.create(nome="EnFerMaGEm")
        self.assertEqual(Curso.objects.count(), 5)
        self.assertEqual(curso.nome, "Enfermagem")

        curso = Curso.objects.create(nome="  engenharia DE PROdução")
        self.assertEqual(Curso.objects.count(), 6)
        self.assertEqual(curso.nome, "Engenharia de Produção")

        curso = Curso.objects.create(nome="pUBLICIDADE E PROpagandA  ")
        self.assertEqual(Curso.objects.count(), 7)
        self.assertEqual(curso.nome, "Publicidade e Propaganda")

        curso = Curso.objects.create(nome=" GESTãO dA QUAlidaDe     ")
        self.assertEqual(Curso.objects.count(), 8)
        self.assertEqual(curso.nome, "Gestão da Qualidade")

        curso = Curso.objects.create(nome="MEDICINA")
        self.assertEqual(Curso.objects.count(), 9)
        self.assertEqual(curso.nome, "Medicina")

        curso = Curso.objects.create(nome="educação FÍSICA")
        self.assertEqual(Curso.objects.count(), 10)
        self.assertEqual(curso.nome, "Educação Física")

        curso = Curso.objects.create(nome="GAStronomia")
        self.assertEqual(Curso.objects.count(), 11)
        self.assertEqual(curso.nome, "Gastronomia")
        
        curso = Curso.objects.create(nome="Ciência da CompuTAÇÃO")
        self.assertEqual(Curso.objects.count(), 12)
        self.assertEqual(curso.nome, "Ciência da Computação")

from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User

class CursoViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='root', password='12345')
        self.client.login(username='root', password='12345')

    def test_cadastrar_curso_view(self):
        url = reverse('cadastrar_curso')
        response = self.client.post(url, {
            'nome': 'engenharia de produção'
        })

        self.assertEqual(response.status_code, 302)  
        self.assertEqual(Curso.objects.count(), 1)
        self.assertEqual(Curso.objects.first().nome, 'Engenharia de Produção')
