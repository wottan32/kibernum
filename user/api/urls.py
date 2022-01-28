from django.conf.urls import url
from django.urls import path, include
from .views import (
    UsuarioListApiView
)

urlpatterns = [
    path('', UsuarioListApiView.as_view()),
]
