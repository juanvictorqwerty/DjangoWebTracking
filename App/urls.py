from django.urls import path

from .views import index ,usersView
from App import views

urlpatterns = [
    path("", index, name="index"),
    path('save-location/', views.save_location, name='save_location'),
]