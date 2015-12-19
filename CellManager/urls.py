"""CellManager URL Configuration
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^upload/$', views.load),
]

# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
