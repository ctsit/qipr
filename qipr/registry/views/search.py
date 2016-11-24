import json

from django.shortcuts import render
from django.http import HttpResponse

from registry.forms import FacetForm
from registry.workflows import search_workflow

def search(request, descriptors_json):
    descriptors = json.loads(descriptors_json or '[]')
    matching_projects = search_workflow.get_matching_projects(descriptors)
    api_data = search_workflow.serialize_for_response(matching_projects, use_natural_keys=True)
    context = {
        'projects': json.loads(api_data),
        'facet_form': FacetForm(),
        'descriptors': descriptors_json or '[]',
    }
    return render(request, 'registry/search.html', context)
