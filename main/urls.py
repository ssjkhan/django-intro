from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("addFriend", views.addFriend, name="addFriend"),
    path("addHobby", views.addHobby, name="addHobby")
]
