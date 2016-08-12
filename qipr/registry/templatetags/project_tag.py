from django import template

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
        'owner_string': __format_owner_string(fields['owner']),
        'owner_id': __get_owner_id(fields['owner']),
    }
    return context

def __format_owner_string(owner_natural_key):
    return ' '.join([str(item) for item in owner_natural_key[2:]])

def __get_owner_id(owner_natural_key):
    return owner_natural_key[0]
