from django.shortcuts import render
from django.http import HttpResponse
from registry.models import Project

def project_info(request, project_id=1):
    if(request.method == "GET"):
        project = Project.objects.get(id=project_id)
        context = {
            'title': project.title,
            'description': project.description,
            'owner': str(project.owner),
            'collaborators_string': '; '.join([str(item) for item in project.collaborator.all()]),
            'advisors_string': '; '.join([str(item) for item in project.advisor.all()]),
            'categories': project.category.all(),
            'mesh_string': ', '.join([str(item) for item in project.mesh_keyword.all()]),
            'bigaim': str(project.big_aim) if project.big_aim else '',
            'clinical_areas': project.clinical_area.all(),
            'clinical_settings': project.clinical_setting.all(),
            'proposed_start_date': project.proposed_start_date,
            'proposed_end_date': project.proposed_end_date,
        }

        return render(request, 'registry/project_info.html', context)
