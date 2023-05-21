from django.shortcuts import render ,redirect,get_object_or_404
from django.contrib.auth import authenticate , login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *


# Create your views here.

def index (request):
    return render(request,'index.html')

def dashboard(request):
    return render(request,'dashboard.html')

def log_in (request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username = username,password= password)
        if user is not None :
            login(request,user )
            return HttpResponseRedirect(reverse(index))
        else:
            return render (request, "login.html", {"message":"Please enter vaild username or password"} )
        
    else:
        return render (request,"login.html")

def menu_and_order(request):
    if request.method == 'POST':
        menu_item_id = request.POST.get('menu_item_id')
        quantity = request.POST.get('quantity')
        order = Order(menu_item_id=menu_item_id, quantity=quantity)
        order.save()
        quantity = 1
        menu_items = MenuItem.objects.all()
        return render(request, 'menu_and_order.html', {'menu_items': menu_items, 'quantity': quantity})
    else:
        menu_items = MenuItem.objects.all()
        return render(request, 'menu_and_order.html', {'menu_items': menu_items})
