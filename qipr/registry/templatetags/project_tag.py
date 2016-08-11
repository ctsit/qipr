from django import template

register = template.Library()

@register.inclusion_tag('templatetags/project_tag.html')
def project_tag(project):
    """
    Renders a project
    takes a project
    """
    context = {
        'project': str(project),
    }
    return context
