from django import template

from registry.models import Person

register = template.Library()

@register.inclusion_tag('templatetags/project_tag.html')
def project_tag(project):
    """
    Renders a project
    takes a project
    """
    fields = project['fields']
    context = {
        'project': str(project),
        'project_id': project['pk'],
        'title': fields['title'],
        'description': fields['description'],
        'owner_string': __get_owner(fields['owner']),
        'owner_id': fields['owner']
    }
    return context

def __get_owner(owner_key):
    return str(Person.objects.get(id=owner_key))
