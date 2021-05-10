from django.shortcuts import render,redirect
from .models import Product,Orders,Cart
from .forms import CreateProductForm,UserRegisterationForm,LoginForm,OrderForm,CartForm
from django.contrib.auth import authenticate,login,logout
from .decorators import user_login,admin_only
# from .authentication import EmailAuthenticateBackend

@admin_only
@user_login
# Create your views here.
def index(request):
    return render(request,'mobile/base.html')

@admin_only
def base(request):
    return render(request,'mobile/index.html')

@user_login
@admin_only
#to list all mobiles
def listmobile(request):
    mobiles=Product.objects.all()
    context={}
    context['mobiles']=mobiles
    return render(request,'mobile/listmobile.html',context)

@admin_only
def adminmobile(request):
    mobiles=Product.objects.all()
    context={}
    context['mobiles']=mobiles
    return render(request,'mobile/adminlist.html',context)

# to add mobile
@admin_only
def add_product(request):
    form=CreateProductForm()
    context={}
    context['form']=form
    if request.method=='POST':
        form=CreateProductForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin')
    return render(request,'mobile/addmobile.html',context)

# function to get id of each mobile
def get_mobile_object(id):
    return Product.objects.get(id=id)

@user_login
# to view mobile details
def mobile_details(request,id):
    mobile=get_mobile_object(id)
    context={}
    context['mobile']=mobile
    return render(request,'mobile/mobiledetails.html',context)

def admin_mobile_details(request,id):
    mobile=get_mobile_object(id)
    context={}
    context['mobile']=mobile
    return render(request,'mobile/adminmobiledetails.html',context)


@admin_only
# to delete a mobile
def delete_mobile(request,id):
    mobile=get_mobile_object(id)
    mobile.delete()
    return redirect('adminlist')

@admin_only
#to update a mobile
def update_mobile(request,id):
    mobile=get_mobile_object(id)
    form=CreateProductForm(instance=mobile)
    context={}
    context['form']=form
    if request.method=='POST':
        form=CreateProductForm(request.POST,instance=mobile,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminlist')

    return render(request,'mobile/mobileupdate.html',context)

# to register
def registeration(request):
    form=UserRegisterationForm()
    context={}
    context['form']=form
    if request.method=='POST':
        form=UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'mobile/login.html',context)
        else:
            form = UserRegisterationForm()
            context['form'] = form
            return redirect('login')
    return render(request,'mobile/registeration.html',context)

#to login
def signin(request):
    form=LoginForm()
    context={}
    context['form']=form
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # obj=EmailAuthenticateBackend()
            # user=obj.authenticate(request,username=username,password=password)
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                if user.is_superuser:
                    return redirect('admin')
                else:
                    return redirect('base')
                return redirect('base')

    return render(request,'mobile/login.html',context)

# to logout
def signout(request):
    logout(request)
    return redirect('login')

#for orders

def item_order(request,id):
    product=get_mobile_object(id)
    form=OrderForm(initial={'user':request.user,'product':product})
    context={}
    context['form']=form
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listmobile')
        else:
            context['form']=form
            return render(request,'mobile/ordereditems.html',context)
    return render(request, 'mobile/ordereditems.html', context)

#to view the order
def view_myorder(request):
    order=Orders.objects.filter(user=request.user)
    context={}
    context['order']=order
    return render(request,'mobile/myorder.html',context)

#to cancel order
def cancel_order(request,id):
    order=Orders.objects.get(id=id)
    order.status='Cancelled'
    order.save()
    return redirect('myorder')

#to add to cart
def add_to_cart(request,id):
    product=get_mobile_object(id)
    form=CartForm(initial={'user':request.user,'product':product})
    context={}
    context['form']=form
    if request.method=='POST':
        form=CartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listmobile')
        else:
            context['form']=form
            return render(request,'mobile/mobiledetails.html',context)
    return render(request, 'mobile/cartitems.html', context)

# to view my cart
def view_mycart(request):
    carts=Cart.objects.filter(user=request.user)
    context={}
    context['carts']=carts
    return render(request,'mobile/cartview.html',context)

#to remove from cart
def remove_cart_item(request,id):
    carts = Cart.objects.get(id=id)
    carts.delete()
    return redirect('listmobile')

#to buy from cart

