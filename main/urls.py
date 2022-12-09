from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("friends", views.allFriends, name="viewFriends"),
    path("friend", views.viewFriend, name="detailFriend"),
    path("addFriend", views.addFriend, name="addFriend"),
    path("foods", views.allFoods, name="viewFood"),
    path("food", views.viewFood, name="detailFood"),
    path("addFood", views.addFood, name="Food"),
    path('signup', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]
