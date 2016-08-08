def set_created_by_if_empty(model, user):
    """
    This function is called by our save function because django
    throws exceptions on object access if something doesn't exist.
    You cannot dereference a related field if it doesn't exist.
    Meaning you have to do a try except block.
    """
    try:
        # the following line throws an exception
        model.created_by is not None
    except:
        model.created_by = user

def get_id_or_none(model):
    """
    Django explodes if you dereference pk before saving to the db
    """
    try:
        return model.id
    except:
        return None

def get_instance_or_none(Model, prop, value):
    try:
        return Model.objects.get(**{prop:value})
    except:
        return None
