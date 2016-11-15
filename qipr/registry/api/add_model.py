from django.http import JsonResponse
# from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from registry.models import User
from registry.workflows import api_workflow
import json
# @approver_login_required
@csrf_exempt
def add_model(request):
    if request.method == 'POST':
        user = User.objects.get(id=1)
        # user = None
        data = api_workflow.translate_and_add_model(user, request.body.decode('utf-8'))
        return JsonResponse({'body': request.body.decode('utf-8')}, safe=False)
