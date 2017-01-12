from django.conf.urls import url
from registry import views
from registry import api

urlpatterns = [
    url(r'^search/(?:s=(?P<search_text>[\w\s]*)/)?(?:d=(?P<descriptors_json>\[.*\])/)?$', views.search, name='search'),
    url(r'^project_info/(?P<project_id>[0-9]+)/$',views.project_info, name='project_info'),
    url(r'^$',views.index, name='index'),
    url(r'^api/add_model/(?P<req_hash>[0-9a-fA-F]+)$', api.add_model, name='add_model'),
]
