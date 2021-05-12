from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from .models import Cart,Orders



class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","password1","password2","email"]

class CartForm(ModelForm):
    class Meta:
        model=Cart
        fields='__all__'
        widgets = {
            'product': forms.Select(attrs={'class': 'text_inp', 'placeholder': 'Product'}),
            'user': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'User'}),
            'quantity': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'Quantity'}),
        }

class OrderForm(ModelForm):
    class Meta:
        model=Orders
        fields=['address','product','user']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'Address'}),
            'product': forms.Select(attrs={'class': 'text_inp', 'placeholder': 'Product'}),
            'user': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'User'})


        }

