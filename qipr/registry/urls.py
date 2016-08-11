from django.conf.urls import url
from registry import views
from registry import api

urlpatterns = [
    url(r'^(?:d=(?P<descriptors_json>\[.*\])/)?$', views.index, name='index'),
]
