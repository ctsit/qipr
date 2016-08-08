from django.http import JsonResponse
from django.contrib.auth.models import User

from registry.workflows import api_workflow

# @approver_login_required
def add_model(request):
    if request.method = 'POST':
        # user = User.objects.get(id=1)
        user = None
        data = api_workflow.translate_and_add_model(user, request.POST)
        return JsonResponse(data)
