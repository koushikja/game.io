from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from gamer_zone.models import *
# Create your views here.

def signup(request):
    if request.method=="POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get("email")
        user_phone=request.POST.get("user_phone")
        
        exists = User.objects.filter(username=username).exists()
        
        if not exists:
            user_info = User.objects.create_user(username,email,password)
            profile = UserDetail.objects.create(user_info=user_info,user_phone=user_phone)
            profile.save()
            return redirect('/login/')
    return render(request,"signup.html")



def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect(f"/{user.pk}/home/")
            

        elif user is None:
            return redirect(f'/login/')
        else:
            # Return an 'invalid login' error message.
            return HttpResponse('invalid user')
    return render(request,"signin.html")



def signout(request):
    logout(request)
    return redirect(f'/login/')

@login_required
def games(request,user_id):
    user = request.user
    games = Game.objects.all()
    return render(request,"games.html",{"games":games , "user":user})

@login_required
def kitchen(request,user_id):
    user = request.user
    kitchen = Kitchen.objects.all()
    return render(request,"kitchen.html",{"kitchen":kitchen , "user":user})

def game(request,user_id):
    pass


def home(request,user_id):
    return render(request,"home.html")

def playgame(request,user_id):
    pass

def food(request,user_id):
    pass

def placeOrder(request,user_id):
    pass

def finalBill(reques,user_id):
    pass

def payBill(request,user_id):
    pass