"""CellManager URL Configuration
"""
from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^$', views.new),
    url(r'^upload/$', views.load),
    url(r'^(?P<id>[A-Z0-9]{10})/$', views.show),
    url(r'^help/$', RedirectView.as_view(url='../static/help.pdf')),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
