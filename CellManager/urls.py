"""CellManager URL Configuration
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.new),
    url(r'^upload/$', views.load),
    # url(r'^(?P<id>[A-Z0-9]{10})$', views.show),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
