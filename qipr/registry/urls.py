from django.conf.urls import url
from registry import views
from registry import api

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/search_projects$', api.search_projects, name='search_projects'),
]
