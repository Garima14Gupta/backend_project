# backend_app/models.py
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    technologies = models.TextField()
    frontend_skills = models.TextField()
    backend_skills = models.TextField()
    databases = models.TextField()
    infrastructure = models.TextField()
    availability = models.CharField(max_length=100)

    class Meta:
        app_label = 'backend_app'  # Specify the app label

    def __str__(self):
        return self.title
