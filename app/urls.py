from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    path('api/', include('app.api.urls.py')),
]
