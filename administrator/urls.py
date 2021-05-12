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
from .views import home,list_all_mobiles,create_mobile,admin_login,admin_logout,mobile_details,delete_mobile,update_mobile

urlpatterns = [

   path('home/',home,name="home"),
   path('list/',list_all_mobiles,name="list"),
   path('create/',create_mobile,name="create"),
   path('login',admin_login,name="login"),
   path('logout',admin_logout,name="logout"),
   path('mobiledetails/<int:id>',mobile_details,name="mobiledetails"),
    path('deletemobile/<int:id>',delete_mobile,name="deletemobile"),
    path('updatemobile/<int:id>',update_mobile,name="updatemobile"),
]
