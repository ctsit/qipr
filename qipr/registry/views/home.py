
from django.shortcuts import render

def home(request):
 
    return render(request, 'registry/home.html')
