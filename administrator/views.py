from django.shortcuts import render,redirect
from .forms import MobileCreateForm
from .models import Mobile
from django.contrib.auth import authenticate,login,logout
from user.models import *
# Create your views here.
def home(request):
    if request.user.is_superuser:
        return render(request,"administrator/index.html")
    else:
        return redirect("login")



def create_mobile(request):
    if request.user.is_superuser:
        form=MobileCreateForm()
        context={}
        context["form"]=form
        if request.method=="POST":
            form=MobileCreateForm(request.POST,files=request.FILES)
            if form.is_valid():
                form.save()
                return redirect("list")
            else:
                pass
        return render(request,"administrator/createmobile.html",context)
    else:
        return redirect("logout")
def list_all_mobiles(request):
    if request.user.is_superuser:
        mobiles=Mobile.objects.all()
        context={}
        context["mobiles"]=mobiles
        return render(request,"administrator/list.html",context)
    else:
         return redirect("logout")

def admin_login(request):
    if request.method== "POST":
        username=request.POST.get("username")
        password = request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect("home")
        else:
            pass
    return render(request,"administrator/login.html")
def admin_logout(request):
    logout(request)
    return redirect("login")

def mobile_details(request,id):
    if request.user.is_superuser:
        mobile=Mobile.objects.get(id=id)
        context={}
        context["mobile"] =mobile
        return render(request,"administrator/view.html",context)
    else:
         return redirect("logout")
def delete_mobile(request,id):
    if request.user.is_superuser:
        mobile = Mobile.objects.get(id=id)
        mobile.delete()
        return redirect("list")
    else:
         return redirect("logout")
def update_mobile(request,id):
    if request.user.is_superuser:
        mobile=Mobile.objects.get(id=id)
        form=MobileCreateForm(instance=mobile)
        context={}
        context["form"] =form
        if request.method=="POST":
            form=MobileCreateForm(request.POST,files=request.FILES,instance=mobile)
            if form.is_valid():
                form.save()
                return redirect("list")
        return render(request, "administrator/update.html", context)
    else:
        return redirect("logout")


def admin_view_order(request):
    if request.user.is_superuser:
        orders=Orders.objects.all()
        context={}
        context["orders"]=orders
        return render(request,"administrator/orderadmin.html",context)
    else:
        return redirect("logout")

def order_delivered(request,id):
    if request.user.is_superuser:
        order=Orders.objects.get(id=id)
        order.status='Delivered'
        order.save()
        return redirect("adminorder")
    else:
        return redirect("logout")


def order_shipped(request,id):
    if request.user.is_superuser:
        order=Orders.objects.get(id=id)
        order.status='Shipped'
        order.save()
        return redirect("adminorder")
    else:
        return redirect("logout")

