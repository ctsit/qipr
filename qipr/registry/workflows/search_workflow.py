from django.core import serializers

from registry.models import Project

def get_matching_projects(descriptors):
    # match them to what they represent in the database
    # repetedly filter projects based on what descriptors we have
    # serialize the project in a meaningful way
    # we might need to define natural_key on the model and get_by_natural_key on the model manager
    # return that project
    pass

def serialize_for_response(items, use_natural_keys=False):
    # serialize the objects
    # return those objects
    pass

def __jsonify(iterable, use_natural_keys=False):
    pass
