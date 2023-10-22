from django.urls import path
from .views import ProjectList, ProjectDetail, ProjectSearch

urlpatterns = [
    path('projects/', ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
    path('projects/search/', ProjectSearch.as_view(), name='project-search'),

]