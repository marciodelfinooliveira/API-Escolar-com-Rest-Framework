from rest_framework import viewsets
from apps.alunos.api.serializers import AlunoSerializer
from apps.alunos.models import AlunoModel
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class AlunoViewSet(viewsets.ModelViewSet):
        
    queryset = AlunoModel.objects.all()
    serializer_class = AlunoSerializer
    

# A classe abaixo é uma view que aplica uma paginação a entidade AlunoModel
class AlunosPag(AlunoViewSet):
        
    pagination_class = PageNumberPagination  # Aplica a paginação a esta view
    queryset = AlunoModel.objects.all()  # Consulta

    def get(self, request):
        page = self.paginate_queryset(self.queryset)  # Consulta
        if page is not None:
            serializer = AlunoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AlunoSerializer(self.queryset, many=True)
        return Response(serializer.data)