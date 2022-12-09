from django.shortcuts import render, redirect
from django.views.generic import ListView
from . import forms

# Create your views here.

def home(req):
    # return (req, )
    return render(req, 'home.html')

def allFriends(req):
    pass

def allHobbies(req):
    pass

def addFriend(req):
    pass

def addHobby(req):
    pass

def viewFriend(req):
    pass

def viewHobby(req):
    pass