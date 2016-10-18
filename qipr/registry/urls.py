from django.conf.urls import url
from registry import views
from registry import api

urlpatterns = [
    url(r'^search/(?:d=(?P<descriptors_json>\[.*\])/)?$', views.search, name='search'),
    url(r'^project_info/(?P<project_id>[0-9]+)/$',views.project_info, name='project_info'),
    url(r'^home/$',views.home, name='home'),
]
