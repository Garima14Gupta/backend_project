# import_data.py
import pandas as pd
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_project.settings')
django.setup()

from backend_app.models import Project

excel_file = "assets/data.xlsx"

data = pd.read_excel(excel_file)

for index, row in data.iterrows():
    Project.objects.create(
        title=row['Project.Title'],
        technologies=row['Project.Technologies'],
        frontend_skills=row['Technical_Skillset.Frontend'],
        backend_skills=row['Technical_Skillset.Backend'],
        databases=row['Technical_Skillset.Databases'],
        infrastructure=row['Technical_Skillset.Infrastructre'],
        availability=row['Other_Information.Availability']
    )

print("Data import completed.")
