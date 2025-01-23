from django.urls import path

from .views import index 
from App import views
from .views import usersView


urlpatterns = [
    path("", index, name="index"),
    path('save-location/', views.save_location, name='save_location'),
    path('get-latest-coordinates/', views.get_latest_coordinates, name='get_latest_coordinates'),
    path('usersView/', views.usersView, name='usersView'),
]