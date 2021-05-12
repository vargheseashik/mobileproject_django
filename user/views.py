from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import UserRegistrationForm,CartForm,OrderForm
from administrator.models import Mobile
from .models import *
from django.db.models import Sum


# Create your views here.
# Create your views here.
def user_home(request):
    return render(request,"user/index.html")

def user_list_all_mobiles(request):
        mobiles=Mobile.objects.all()
        context={}
        context["mobiles"]=mobiles
        return render(request,"user/list.html",context)

def user_login(request):
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

def user_logout(request):
    logout(request)
    return redirect("userlist")

def user_mobile_details(request,id):
        mobile=Mobile.objects.get(id=id)
        context={}
        context["mobile"] =mobile
        return render(request,"user/view.html",context)

def user_registration(request):
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

def add_to_cart(request,id):
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

# to view my cart
def view_mycart(request):
    carts=Cart.objects.filter(user=request.user)
    #context= {}
    #context['carts']=carts
    total=Cart.objects.filter(user=request.user).aggregate(Sum('price_total'))
    return render(request,'user/cartview.html', {'carts':carts,'total':total})

#to remove from cart
def remove_cart_item(request,id):
    carts = Cart.objects.get(id=id)
    carts.delete()
    return redirect('mycart')

# function to get id of each mobile
def get_mobile_object(id):
    return Mobile.objects.get(id=id)

#to buy from cart
def cart_order(request,id):
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

def user_list_all_orders(request):
    order = Orders.objects.filter(user=request.user)
    context = {}
    context['order'] = order
    return render(request, 'user/myorder.html', context)

#to cancel order
def cancel_order(request,id):
    order=Orders.objects.get(id=id)
    order.status='Cancelled'
    order.save()
    return redirect('myorders')




