from django.shortcuts import render
from django.http import HttpResponse
from registry.models import *

# Create your views here.
def project_info(request,project_id=1):
	if(request.method == "GET"):
		project = Project.objects.filter(id=project_id),
		context = {
			'projects': {'title':'project.title'},
			'project' : project 
			
		}
		return render(request,'registry/project_info.html',context) 