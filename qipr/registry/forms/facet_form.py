from registry.models import *
from operator import attrgetter

related_by_projects_Models = [
    BigAim,
    ClinicalArea,
    ClinicalSetting,
    Descriptor,
]


class FacetForm:
    def __init__(self):
        self.facet_categories = [model.__name__ for model in related_by_projects_Models]
        for model in related_by_projects_Models:
            models = list(model.objects.all())
            models.sort(key=lambda m : m.projects.count(), reverse=True)
            setattr(self, model.__name__, models)

    def get_display(self, facet_category):
        displays = {
            'BigAim': 'Big Aim',
            'ClinicalArea': 'Clinical Area',
            'ClinicalSetting': 'Clinical Setting',
            'Descriptor': 'MeSH Keyword',
        }
        return displays[facet_category]

