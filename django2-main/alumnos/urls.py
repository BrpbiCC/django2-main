from django.urls import path 
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('lista', views.index, name='lista'),
]
