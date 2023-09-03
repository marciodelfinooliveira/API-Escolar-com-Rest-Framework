from rest_framework import viewsets
from apps.cursos.api.serializers import CursoSerializer
from apps.cursos.models import CursoModel
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CursoViewSet(viewsets.ModelViewSet):
    
    queryset = CursoModel.objects.all()
    serializer_class = CursoSerializer

# A classe abaixo é uma view que aplica uma paginação a entidade CursoModel
class CursosPag(CursoViewSet):
    
    PageNumberPagination.page_size = 2
    pagination_class = PageNumberPagination  # Aplica a paginação a esta view
    queryset = CursoModel.objects.all()  # Consulta

    def get(self, request):
        page = self.paginate_queryset(self.queryset)  # Consulta
        if page is not None:
            serializer = CursoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CursoSerializer(self.queryset, many=True)
        return Response(serializer.data)