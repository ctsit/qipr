import json
import importlib
import datetime
import dateutil.parser as date_parser

from registry import constants
from registry import utils
from registry.translation.RelatedStore import RelatedStore

def translate(user, json_data):
    """
    Takes json from post data and turns it into a python data
    structure. Then it iterates over it and returns a list
    of instantiated models
    """
    deserialized = json.loads(json_data)
    return [get_model(item, user) for item in deserialized]

def get_model(serialized_model, user):
    """
    In order to instantiate the serialized model we need
    the constructor and we need to transform the natural
    dictionary representation into something that we can
    pass to the constructor as kwargs.
    """
    Model = get_model_class(serialized_model)
    (initial_field, relatedStore) = get_initial_values(serialized_model, save_as(user))
    return create_or_update(Model, initial_field, save_as(user), relatedStore)

def get_model_class(serialized_model):
    model_name = get_model_name(serialized_model)
    return model_name_to_model_class(model_name)

def get_model_name(serialized_model):
    """
    Extracts the model's name from the serialized model
    """
    return serialized_model.get('fields').get('model_class_name')

def model_name_to_model_class(model_class_name):
    """
    Given a model_class_name, this function returns the corresponding
    constructor.
    """
    module_name = 'registry.models'
    constructor_name = model_class_name_to_constructor(model_class_name)
    models_module = importlib.import_module(module_name)
    return getattr(models_module, constructor_name)

def model_class_name_to_constructor(model_class_name):
    """
    This function is to serve as a template for future translation
    modules. This should be a mapping from the 'model_class_name'
    field to the correct model constructor.
    """
    return model_class_name

def get_initial_values(serialized_model, user_save):
    """
    This function gets the initial values out of the fields dictionary
    in the serialized_model

    We need to do some things to the fields before they are ready to be passed
    as kwargs to the constructor.

    1) fix provenance
    2) replace serialized related models with an instantiated model
    """
    model_name = get_model_name(serialized_model)
    copy = dict(serialized_model.get('fields'))
    copy = fix_provenance(copy)
    copy = remove_model_class_name_field(copy)
    (copy, relatedStore) = get_fields_related_store(model_name, copy, user_save)
    del serialized_model['fields']
    serialized_model['fields'] = copy
    return (serialized_model['fields'], relatedStore)

def remove_model_class_name_field(fields):
    """
    When reconstituting the models, they dont know how to deal with this
    extra field we added. We need to get rid of it.
    """
    del fields['model_class_name']
    return fields

def fix_provenance(fields):
    """
    This function is to here because much or the logic surrounding
    the provenance fields related to the database, and seeing that
    we are taking information from some database and putting it in
    another, we need to be able to fix those fields.
    """
    provenance_fields = [
        'created',
        'created_by',
        'last_modified',
        'last_modified_by',
    ]
    for field in provenance_fields:
        try:
            del fields[field]
        except:
            pass
    return fields

def get_fields_related_store(model_name, fields, user_save):
    """
    This function's purpose is to replace the values in fields
    that correspond to related models in the fields dictionary
    with instances of the model.
    """
    fields = flatten_related_values(fields)
    (fields, relatedStore) = instantiate_related_models(fields, user_save)
    return (fields, relatedStore)

def flatten_related_values(fields_to_change):
    """
    This function takes fields, and a key and returns the
    natural dict or list for that key to a related model.
    """
    fields = dict(fields_to_change)
    for key in fields.keys():
        value = fields.get(key)
        # either the value is a list of related models or one dict
        if isinstance(value, list) and len(value) >= 1:
            # when we have many models
            if isinstance(value[0], list):
                #flatten it out
                fields[key] = [item[0] for item in value]
    return fields

def make_model_from_dict(item, user_save):
        natural_dict = item
        model_class_name = item.get('model_class_name')
        Model = model_name_to_model_class(model_class_name)
        natural_dict = fix_provenance(natural_dict)
        natural_dict = remove_model_class_name_field(natural_dict)
        return create_or_update(Model, natural_dict, user_save)

def instantiate_related_models(fields, user_save):
    """
    This function iterates over the properties of
    fields and if the dictionary has a model_class_name
    property then it will call create or update on that
    dictionary with the right constructor
    """
    to_delete = set();
    relatedStore = RelatedStore();

    for key in fields.keys():
        value = fields.get(key)
        if isinstance(value, list):
            if len(value) == 0:
                to_delete.add(key)
            for item in value:
                if isinstance(item, dict) and item.get('model_class_name'):
                    to_delete.add(key)
                    instance = make_model_from_dict(item, user_save)
                    relatedStore.add_related(key, instance)
        else:
            if isinstance(value, dict) and value.get('model_class_name'):
                to_delete.add(key)
                instance = make_model_from_dict(value, user_save)
                relatedStore.add_related(key, instance)

    for key in to_delete:
        del fields[key]
    return (fields, relatedStore)

def create_or_update(Model, natural_dict, user_save, relatedStore=None):
    """
    Checks for a guid. If it finds one, it tries to get the
    corresponding element and update it. Otherwise it will
    instantiate a new one.
    """
    guid = natural_dict.get('guid')
    # need to remove invalid things in the natural dict
    instance = utils.get_instance_or_none(Model, 'guid', guid)
    if instance == None:
        instance = Model()
    for key in natural_dict.keys():
        value = natural_dict.get(key)
        if ('time' in key) and value:
            value = date_parser.parse(value)
        if ('date' in key) and value:
            value = date_parser.parse(value)
        setattr(instance, key, value)
    if relatedStore:
        user_save(instance)
        relatedStore.associate_relateds(instance)
    user_save(instance)
    return instance

def save_as(user):
    """
    Returns a callback which saves the model as the user that you
    pass in
    """
    def user_save(instance):
        instance.save(user)

    return user_save
