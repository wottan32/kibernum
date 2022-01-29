from django.urls import path
from .api import usuario_api_view, usuario_detail_api_view

urlpatterns = [
    path('usuario/', usuario_api_view, name='usuario_api'),
    path('usuario/<int:pk>/', usuario_detail_api_view, name='usuario_detail_api_view')
]
