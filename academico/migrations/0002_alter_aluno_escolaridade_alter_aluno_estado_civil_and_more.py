# Generated by Django 5.1.7 on 2025-05-07 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='escolaridade',
            field=models.CharField(choices=[('fun', 'Fundamental'), ('med', 'Médio'), ('sup', 'Superior'), ('pos', 'Pós-graduação'), ('mes', 'Mestrado'), ('dou', 'Doutorado')], max_length=50),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='estado_civil',
            field=models.CharField(choices=[('S', 'Solteiro'), ('C', 'Casado'), ('D', 'Divorciado'), ('V', 'Viúvo')], max_length=30),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('NB', 'Não-binário'), ('O', 'Outro')], max_length=2),
        ),
    ]
