from django.shortcuts import render, redirect

# Create your views here.

def home(req):
    # return (req, )
    return render(req, 'home.html')


def update(req):
    data = {
        "title": "Update Page",
        "body": "THIS IS UPDATE"
    }
    return render(req,'base.html',data)

def new(req):
    
    data = {
        "title": "New Page",
        "body": "THIS IS NEW"
    }

    return render(req, 'base.html', data)