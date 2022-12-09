from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("friends", views.allFriends, name="viewFriends"),
    path("friend", views.viewFriend, name="detailFriend"),
    path("addFriend", views.addFriend, name="addFriend"),
    path("hobbies", views.allHobbies, name="viewHobibes"),
    path("hobby", views.viewHobby, name="detailHobby"),
    path("addHobby", views.addHobby, name="addHobby"),
]
