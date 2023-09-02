from rest_framework import routers
from apps.professores.api.viewsets import ProfessorViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('', ProfessorViewSet, basename='Professor')

urlpatterns = [
    path('', include(router.urls)),
]