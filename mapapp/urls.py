from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('locations/', views.get_locations, name='get_locations'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('add_location/', views.add_location, name='add_location'),
    path('indexnotauthen/', views.indexnotauthen, name='indexnotauthen'),
    path('locations/<int:location_id>/delete/', views.delete_location, name='delete_location'), 
]