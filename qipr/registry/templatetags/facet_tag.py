from django import template

register = template.Library()

@register.inclusion_tag('templatetags/facet_tag.html')
def facet_tag(facet_category):
    """
    Renders a catergory of facets
    use with FacetForm
    """
    context = {
        'category': None,
        'facets': []
    }
    # fill facets with information that was passed in from the form
    # context['facets'] = __facet_dict_from_model_list(models)
    return context

def __facet_dict_from_model_list(models):
    facets
    for model in models:
        filter_field = __get_filter_field(model)
        facet_dict = {
            'filter-field': None,
            'value': None,
            'name': None,
            'label': None,
        }
    return facet_dict
