# Generated by Django 4.2.4 on 2023-09-02 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professormodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
