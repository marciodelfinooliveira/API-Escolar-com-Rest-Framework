from rest_framework.viewsets import ModelViewSet
from apps.user.models import User
from .serializers import UserSerializer

class UserViewSet(ModelViewSet):

# Pega odos os dados que estao na tabela Task
    queryset = User.objects.all()

# O que retorna ao usuário
    serializer_class = UserSerializer

