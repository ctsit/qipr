import json

from django.shortcuts import render
from django.http import HttpResponse

from registry.forms import FacetForm
from registry.workflows import search_workflow

def search(request, search_text, descriptors_json):
    descriptors = json.loads(descriptors_json or '[]')
    matching_projects = search_workflow.get_matching_projects(search_text, descriptors)
    api_data = search_workflow.serialize_for_response(matching_projects, use_natural_keys=True)
    context = {
        'projects': json.loads(api_data),
        'facet_form': FacetForm(),
        'descriptors': descriptors_json or '[]',
        'search_query': search_text or '',
    }
    return render(request, 'registry/search.html', context)
