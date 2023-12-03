from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect("index")
    context={}
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user=auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("index")
        else:
            context={
                "error":"Kullanıcı Adı Yada Şİfre Hatalı",
            }
    
    return render(request,"account/login.html",context)

def register(request):
    if request.user.is_authenticated:
        return redirect("index")
    context={
        "error":[]
    }
    if request.method=="POST":
        username = request.POST["username"]
        email=request.POST["email"]
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        password = request.POST["password"]
        repassword=request.POST["repassword"]

        if password != repassword:
            context["error"].append("Şifre Hatalı")
        if User.objects.filter(username=username).exists():
            context["error"].append("Kullanıcı Adı Mevcut")
        if User.objects.filter(email=email):
            context["error"].append("Email Mevcut") 
        
        if password == repassword:
            if not(User.objects.filter(username=username).exists()):
                if not(User.objects.filter(email=email).exists()):
                    user=User.objects.create_user(username=username,email=email,first_name=firstname,
                                                  last_name=lastname,password=password)
                    user.save()
                    return redirect("login")
    return render(request,"account/register.html",context)

def logout(request):
    auth.logout(request)
    return redirect("index")
