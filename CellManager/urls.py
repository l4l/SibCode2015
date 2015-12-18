"""CellManager URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^upload/.*$', views.load),
    url(r'^download/(?P<file_id>[0-9]+)/$', views.download),
    url(r'^admin/', include(admin.site.urls)),
]
