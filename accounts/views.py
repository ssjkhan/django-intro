from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.




def signup(req):
    if req.method == "GET":
        return render (req, 'signup.html', {'form' : SignUpForm})
    else:
        vars = req.POST

        if vars.get

def logout(req):
    pass

def login(req):
    pass

