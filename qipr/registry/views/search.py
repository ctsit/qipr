import json

from django.shortcuts import render

from registry.forms import FacetForm
from registry.workflows import search_workflow
import registry.constants as constants

def search(request, search_text, descriptors_json):
    descriptors = json.loads(descriptors_json or '[]')
    matching_projects = search_workflow.get_matching_projects(search_text, descriptors)
    api_data = search_workflow.serialize_for_response(matching_projects, use_natural_keys=True)
    context = {
        'projects': json.loads(api_data),
        'facet_form': FacetForm(),
        'descriptors': descriptors_json or '[]',
        'search_query': search_text or '',
        'approver_dashboard': constants.approver_url + '/dashboard',
        'approver_logout': constants.approver_url + '/logout',
        'approver_url': constants.approver_url,
    }
    return render(request, 'registry/search.html', context)
