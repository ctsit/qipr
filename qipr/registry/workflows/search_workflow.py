from django.core import serializers

from registry.models import Project

def get_matching_projects(search_text, descriptors):
    """
    gets projects that match successive filter calls from descriptors

    descriptors is a list of ff, v dictionaries
    where ff is the left hand side of the filter keyword arguments call
    and v is the right hand side of the filter keyword arguments call
    """
    """
    Right now this is strongly coupled to the model
    think about how to decouple
    """
    projects = Project.objects.all()
    filter_field_key = 'ff'
    value_key = 'v'
    for item in descriptors:
        projects = projects.filter(**{item[filter_field_key]: item[value_key]})
    if search_text:
        title_projects = projects.filter(title__icontains=search_text)
        desc_projects = projects.filter(description__icontains=search_text)
        projects = list(title_projects) + list(desc_projects)
    return projects

def serialize_for_response(iterable, use_natural_keys=False):
    return serializers.serialize('json', iterable, use_natural_foreign_keys=use_natural_keys)
