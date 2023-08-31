from rest_framework.viewsets import ModelViewSet
from apps.todo.models import Task
from .serializers import TaskSerializer

class TaskViewSet(ModelViewSet):

# Pega odos os dados que estao na tabela Task
    queryset = Task.objects.all()

# O que retorna ao usuário
    serializer_class = TaskSerializer

