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
from .views import user_home,user_list_all_mobiles,user_login,user_logout,user_mobile_details,user_registration,add_to_cart,view_mycart,remove_cart_item,cart_order,user_list_all_orders,cancel_order

urlpatterns = [
   path('home/',user_home,name="userhome"),
   path('',user_list_all_mobiles,name="userlist"),
   path('login',user_login,name="userlogin"),
   path('logout',user_logout,name="userlogout"),
   path('mobiledetails/<int:id>',user_mobile_details,name="usermobiledetails"),
   path('registration',user_registration,name="userregistration"),
   path('addcart/<int:id>',add_to_cart,name='addcart'),
   path('mycart',view_mycart,name='mycart'),
   path('remove/<int:id>',remove_cart_item,name='remove'),
   path('order/<int:id>',cart_order,name='placeorder'),
   path('myorders/',user_list_all_orders,name='myorders'),
   path('cancelorders/<int:id>',cancel_order,name='cancelorders'),
]
