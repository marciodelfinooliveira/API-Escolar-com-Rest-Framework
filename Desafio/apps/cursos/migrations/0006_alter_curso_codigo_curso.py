# Generated by Django 4.2.4 on 2023-09-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0005_alter_curso_codigo_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='codigo_curso',
            field=models.CharField(max_length=6, unique=True),
        ),
    ]
