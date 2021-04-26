from django.urls import path, include
from . import views

app_name='tp'

urlpatterns = [
    path('', views.homeView, name='homeView')
]

