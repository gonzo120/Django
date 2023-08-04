from projects.models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
  queryset = Project.objects.all() #consultamos todos los objetos
  permission_classes = [permissions.AllowAny]
  serializer_class = ProjectSerializer