from registry.translation import approver as translation_module

def translate_and_add_model(user, post_data):
    """
    This function is what is called by the api to build a
    registry model from an approver model.
    """
    try:
        registry_models = translation_module.translate(post_data)
        for model in registry_models:
            model.save(user)
    except:
        # these are the required things we need first
        pass

    # return data about how it all went, error if lacking relateds

