from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import UserRegistrationForm,CartForm,OrderForm
from administrator.models import Mobile
from .models import *
from django.db.models import Sum


# Create your views here.
def user_home(request):
    if request.user.is_authenticated:
        return render(request,"user/index.html")
    else:
        return redirect("userlogin")

def user_list_all_mobiles(request):
    if request.user.is_authenticated:
        mobiles=Mobile.objects.all()
        context={}
        context["mobiles"]=mobiles
        return render(request,"user/list.html",context)
    else:
        return redirect("userlogin")

def user_login(request):
    if request.user.is_authenticated:
        if request.method== "POST":
            username=request.POST.get("username")
            password = request.POST.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("userhome")
            else:
                pass
        return render(request,"user/login.html")
    else:
        return redirect("userlogin")


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("userlist")
    else:
        return redirect("userlogin")

def user_mobile_details(request,id):
    if request.user.is_authenticated:
        mobile=Mobile.objects.get(id=id)
        context={}
        context["mobile"] =mobile
        return render(request,"user/view.html",context)
    else:
        return redirect("userlogin")

def user_registration(request):
    if request.user.is_authenticated:
        form=UserRegistrationForm()
        context = {}
        context["form"] = form
        if request.method == "POST":
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("userlogin")
            else:
                context["form"] = form
                return render(request, "user/registration.html", context)

        return render(request, "user/registration.html", context)
    else:
        return redirect("userlogin")

def add_to_cart(request,id):
    if request.user.is_authenticated:
        product=get_mobile_object(id)
        form=CartForm(initial={'user':request.user,'product':product})
        context={}
        context['form']=form
        if request.method=='POST':
            form=CartForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('mycart')
            else:
                context['form']=form
                return render(request,'user/view.html',context)
        return render(request, 'user/cartitems.html', context)
    else:
        return redirect("userlogin")

# to view my cart
def view_mycart(request):
    if request.user.is_authenticated:

        carts=Cart.objects.filter(user=request.user)
        #context= {}
        #context['carts']=carts
        total=Cart.objects.filter(user=request.user).aggregate(Sum('price_total'))
        return render(request,'user/cartview.html', {'carts':carts,'total':total})
    else:
        return redirect("userlogin")

#to remove from cart
def remove_cart_item(request,id):
    if request.user.is_authenticated:
        carts = Cart.objects.get(id=id)
        carts.delete()
        return redirect('mycart')
    else:
        return redirect("userlogin")

# function to get id of each mobile
def get_mobile_object(id):
        return Mobile.objects.get(id=id)

#to buy from cart
def cart_order(request,id):
    if request.user.is_authenticated:
        carts=Cart.objects.get(id=id)
        form=OrderForm(initial={'user':request.user,'product':carts.product})
        context={}
        context['form']=form
        if request.method=='POST':
            form=OrderForm(request.POST)
            if form.is_valid():
                form.save()
                remove_cart_item(request,id)
                return redirect('mycart')
            else:
                context['form']=form
                return render(request,'user/ordereditems.html',context)
        return render(request, 'user/ordereditems.html', context)
    else:
        return redirect("userlogin")

def user_list_all_orders(request):
    if request.user.is_authenticated:
        order = Orders.objects.filter(user=request.user)
        context = {}
        context['order'] = order
        return render(request, 'user/myorder.html', context)
    else:
        return redirect("userlogin")

#to cancel order
def cancel_order(request,id):
    if request.user.is_authenticated:
        order=Orders.objects.get(id=id)
        order.status='Cancelled'
        order.save()
        return redirect('myorders')
    else:
        return redirect("userlogin")




