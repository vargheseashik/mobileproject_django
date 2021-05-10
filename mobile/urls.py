"""mobileproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import index,base,listmobile,add_product,mobile_details,update_mobile,delete_mobile,\
    registeration,signin,signout,item_order,view_myorder,cancel_order,adminmobile,admin_mobile_details,\
    add_to_cart,view_mycart,remove_cart_item



urlpatterns = [
    path('userhome',index,name='base'),
    path('adminhome',base,name='admin'),
    path('list',listmobile,name='listmobile'),
    path('adminlist',adminmobile,name='adminlist'),
    path('add',add_product,name='addproduct'),
    path('details/<int:id>',mobile_details,name='mobdetails'),
    path('admindetails/<int:id>', admin_mobile_details, name='adminmobdetails'),
    path('update/<int:id>',update_mobile,name='update'),
    path('delete/<int:id>',delete_mobile,name='delete'),
    path('registeration',registeration,name='register'),
    path('login',signin,name='login'),
    path('logout',signout,name='logout'),
    path('ordered/<int:id>',item_order,name='order'),
    path('myorder',view_myorder,name='myorder'),
    path('cancelorder/<int:id>', cancel_order, name='cancelorder'),
    path('addcart/<int:id>',add_to_cart,name='addcart'),
    path('mycart',view_mycart,name='mycart'),
    path('remove/<int:id>',remove_cart_item,name='remove'),

]
