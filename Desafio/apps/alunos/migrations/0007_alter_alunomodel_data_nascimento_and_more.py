# Generated by Django 4.2.4 on 2023-09-07 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0006_remove_alunomodel_curso_matriculado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunomodel',
            name='data_nascimento',
            field=models.DateField(unique=True),
        ),
        migrations.AlterField(
            model_name='alunomodel',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]