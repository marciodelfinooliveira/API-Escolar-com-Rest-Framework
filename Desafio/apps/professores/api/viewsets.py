from rest_framework import viewsets
from apps.professores.api.serializers import ProfessorSerializer
from apps.professores.models import ProfessorModel
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
class ProfessorViewSet(viewsets.ModelViewSet):
    
    queryset = ProfessorModel.objects.all()
    serializer_class = ProfessorSerializer

# A classe abaixo é uma view que aplica uma paginação a entidade ProfessorModel
class ProfessorPag(ProfessorViewSet):
    
    PageNumberPagination.page_size = 3
    pagination_class = PageNumberPagination  # Aplica a paginação a esta view
    queryset = ProfessorModel.objects.all()  # Consulta

    def get(self, request):
        page = self.paginate_queryset(self.queryset)  # Consulta
        if page is not None:
            serializer = ProfessorSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ProfessorSerializer(self.queryset, many=True)
        return Response(serializer.data)