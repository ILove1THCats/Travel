from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('locations/', views.get_locations, name='get_locations'),
    path('register/', views.register, name='register'),
]