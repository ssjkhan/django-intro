from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models

# Create your views here.

def signup(req):
    msg = ""

    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('viewFriends')
        else:
            msg = "Invalid credentials - try again"

    
    form  = UserCreationForm()
    context = {'form': form, 'error_message': msg}
    
    return render(req, 'registration/signup.html', context)

def home(req):
    # return (req, )
    return render(req, 'home.html')

def allFriends(req):
    data = models.Friend.objects.all()
    print(data)
    return render(req, )

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