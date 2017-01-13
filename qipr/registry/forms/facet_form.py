from registry.models import *
from operator import attrgetter

facet_Models = [
    BigAim,
    ClinicalArea,
    ClinicalSetting,
    Keyword,
]

class FacetForm:
    def __init__(self):
        self.facet_categories = [model.__name__ for model in facet_Models]
        for model in facet_Models:
            models = list(model.objects.all())
            models.sort(key=lambda m : m.project_set.count(), reverse=True)
            setattr(self, model.__name__, models)

