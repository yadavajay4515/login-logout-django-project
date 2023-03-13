from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate

# Create your views here.


def index(request):
   if request.user.is_anonymous:
    #   return redirect("/index")
        return render(request, "index.html")


def login(request):
   if request.method == "POST":
       username = request.POST.get("username")
       password = request.POST.get("password")
       print(username,password)
    #   check if user has entered the currect directry
       user = authenticate(username=username, password=password)
       if user is not None:
    # A backend authenticated the credentials
         return redirect("/")
       else:
         return render(request, "login.html")
    # No backend authenticated the credentials
   return render(request,"login.html")
def logoutuser(request):
  logout(request)
  return redirect('/login')