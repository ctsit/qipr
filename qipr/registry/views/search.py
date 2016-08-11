import json

from django.shortcuts import render
from django.http import HttpResponse

from registry.workflows import search_workflow

# Create your views here.
def index(request, descriptors_json):
    descriptors = json.loads(descriptors_json or '[]')
    matching_projects = search_workflow.get_matching_projects(descriptors)
    api_data = {
        'test':'it worked',
        'descriptors':descriptors_json,
    }
    api_data = search_workflow.serialize_for_response(matching_projects, use_natural_keys=True)
    context = {
        'projects': json.loads(api_data),
    }
    return render(request, 'registry/index.html', context)
