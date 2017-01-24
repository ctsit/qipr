from django import template

from registry.constants import filter_field_maps

register = template.Library()

@register.inclusion_tag('templatetags/facet_tag.html')
def facet_tag(facet_category, facet_form):
    """
    Renders a catergory of facets
    use with FacetForm
    """
    context = {
        'display': facet_form.get_display(facet_category),
        'facets': []
    }
    # fill facets with information that was passed in from the form
    context['facets'] = [__get_facet_dict(model) for model in getattr(facet_form, facet_category)]
    return context

def __get_facet_dict(model):
    facet_dict = {
        'filter_field': __get_filter_field(model),
        'value': model.pk,
        'name': __get_name(model),
        'label': __get_name(model),
        'is_checked': ''
    }
    return facet_dict

def __get_name(model):
    try:
        name = model.name
        return name
    except:
        name = model.mesh_heading
        return name

def __get_filter_field(model):
    return filter_field_maps[model.__class__.__name__]
