# Generated by Django 5.1.7 on 2025-05-08 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0002_alter_aluno_escolaridade_alter_aluno_estado_civil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(max_length=14, unique=True, verbose_name='digite o cpf: '),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='data_nascimento',
            field=models.DateField(verbose_name='informe a data de nascimento: '),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='escolaridade',
            field=models.CharField(choices=[('fun', 'Fundamental'), ('med', 'Médio'), ('sup', 'Superior'), ('pos', 'Pós-graduação'), ('mes', 'Mestrado'), ('dou', 'Doutorado')], max_length=50, verbose_name='selecione o nível de escolaridade: '),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='estado_civil',
            field=models.CharField(choices=[('S', 'Solteiro'), ('C', 'Casado'), ('D', 'Divorciado'), ('V', 'Viúvo')], max_length=30, verbose_name='selecione o estado civil: '),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('NB', 'Não-binário'), ('O', 'Outro')], max_length=2, verbose_name='selecione o gênero: '),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='digite o nome: '),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='digite o nome: '),
        ),
    ]
