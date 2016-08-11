from django.http import JsonResponse

from registry.workflows import search_workflow

def search_projects(request):
    # accept variadic args
    api_data = {}
    # get the descriptors
    descriptors = []
    matching_projects = search_workflow.get_matching_projects(descriptors)
    api_data = search_workflow.serialize_for_response(matching_projects, use_natural_keys=True)
    return JsonResponse(api_data)
