from rest_framework import routers
from apps.professores.api.viewsets import ProfessorViewSet
from django.urls import path, include


#define as rotas associadas às operações que podem ser 
# realizadas com o app "Professor" 
router = routers.DefaultRouter()
router.register('', ProfessorViewSet, basename='Professor')

urlpatterns = [
    path('', include(router.urls)),
]