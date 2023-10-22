# backend_app/filters.py
import django_filters
from .models import Project


class ProjectNameFilter(django_filters.FilterSet):
    project_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Project
        fields = ['title']
