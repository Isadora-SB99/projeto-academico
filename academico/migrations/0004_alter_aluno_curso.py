# Generated by Django 5.2 on 2025-05-21 23:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0003_alter_aluno_cpf_alter_aluno_data_nascimento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='academico.curso'),
        ),
    ]
