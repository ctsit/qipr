from django.conf.urls import url
from registry import views
from registry import api

urlpatterns = [
    url(r'^(?:d=(?P<descriptors_json>\[.*\])/)?$', views.index, name='index'),
    url(r'^project_info/(?P<project_id>[0-9]+)/$',views.project_info, name='project_info'),
    url(r'^home/$',views.home, name='home'),
]
