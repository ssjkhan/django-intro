from django.shortcuts import render, redirect
from django.views.generic import ListView
from . import forms

# Create your views here.

def home(req):
    # return (req, )
    return render(req, 'home.html')

def allFriends(req):
    pass

def viewFriend(req):
    pass

def addFriend(req):
    pass

def allFoods(req):
    pass

def viewFood(req):
    pass

def addFood(req):
    pass