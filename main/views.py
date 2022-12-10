from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login as auth_login
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
            auth_login(req, user)
            return redirect('viewFriends')
        else:
            msg = "Invalid credentials - try again"

    
    form  = UserCreationForm()
    context = {'form': form, 'error_message': msg}
    
    return render(req, 'registration/signup.html', context)

def login(req):
    return render(req, 'registration/login.html')

def home(req):
    return render(req, 'home.html')

@login_required
def allFriends(req):
    friends = models.Friend.objects.filter(user = req.user)
    favFoods = []
    for friend in friends:
        rest = list(models.Food.objects.exclude(id__in = friend.favFoods.all().values_list('id')).values())
        favFoods.append(rest)

    
    context = {'context' :zip(friends, favFoods)}
    print(context['context'])
    return render(req, 'friends/index.html', context)

@login_required
def viewFriend(req, friend_id):
    friend = models.Friend.get(id=friend_id)
    return render(req, 'friends/detail.html', {'friend':friend})


class AddFriend(LoginRequiredMixin, CreateView):
    model = models.Friend
    fields = ['name', 'favFoods']
    success_url = '/friends'

    def form_valid(self, form):
        form.instance.user = self.request.user

        return  super().form_valid(form)

@login_required
def allFoods(req):
    foods = models.Food.objects.all()
    print(foods)
    return render(req, 'foods/index.html', {'foods': foods})
    
@login_required
def viewFood(req):
    return render(req, 'foods/detail.html')

class AddFood(LoginRequiredMixin, CreateView):
    model = models.Food
    fields = ['name', 'flavour']

    def form_valid(self, form):
        form.instance.user = self.request.user

        return  super().form_valid(form)
    success_url = '/foods'


def addFood(req):
    return render(req, 'foods/add.html')
    