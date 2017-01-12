from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from registry.workflows import api_workflow
from registry.constants import bridge_keys, approver_username

import json
import hashlib

@csrf_exempt
def add_model(request, req_hash):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        user = __get_user_from_hash(data, req_hash)
        if user:
            res_data = api_workflow.translate_and_add_model(user, data)
        return JsonResponse({'body': res_data}, safe=False) if user else HttpResponseForbidden()
    else:
        return HttpResponseForbidden()


def __get_user_from_hash(json_data, req_hash):
    to_hash = json_data.encode('utf-8') + bridge_keys['approver'].encode('utf-8')
    check_hash = hashlib.md5(to_hash).hexdigest()
    if req_hash == check_hash:
        return User.objects.get(username=approver_username)
    return None
