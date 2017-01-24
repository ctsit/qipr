
from django.shortcuts import render

import registry.constants as constants

def index(request):
    context = {
        'approver_dashboard': constants.approver_url + '/dashboard',
        'approver_logout': constants.approver_url + '/logout',
        'approver_url': constants.approver_url,
        'version_number': constants.VERSION,
    }

    return render(request, 'registry/index.html', context)
