from django.urls import include, path

from . import views

urlpatterns = [
    path('clothes/', include('clothes.urls')),
]