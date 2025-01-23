from django.urls import path

from .views import index ,usersView

urlpatterns = [
    path("", index, name="index"),
    path("templates", usersView, name="usersView")
]