# Generated by Django 4.2.4 on 2023-08-31 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='data',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='descricao',
            new_name='description',
        ),
    ]
