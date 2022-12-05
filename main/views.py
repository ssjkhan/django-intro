from django.shortcuts import render, redirect

# Create your views here.

def home(req):
    # return (req, )
    return render(req, 'base.html')