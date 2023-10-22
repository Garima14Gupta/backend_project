# backend_app/views.py
from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Project
from .serializers import ProjectSerializer
from .filters import ProjectNameFilter


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
class ProjectSearch(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProjectNameFilter
