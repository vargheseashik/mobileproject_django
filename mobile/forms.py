from django.forms import ModelForm
from .models import Product,Orders,Cart
from django import forms
from django.contrib.auth.forms import UserCreationForm,User
class CreateProductForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__'

        widgets={
            'product_name':forms.TextInput(attrs={'class':'text_inp'}),
            'price': forms.TextInput(attrs={'class': 'text_inp'}),
            'specs': forms.TextInput(attrs={'class': 'text_inp'}),
            'image': forms.FileInput(attrs={'class': 'text_inp'})

        }

class UserRegisterationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2','email']

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class OrderForm(ModelForm):
    class Meta:
        model=Orders
        fields=['address','product','user']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'Address'}),
            'product': forms.Select(attrs={'class': 'text_inp', 'placeholder': 'Product'}),
            'user': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'User'})


        }

class CartForm(ModelForm):
    class Meta:
        model=Cart
        fields='__all__'
        widgets = {
            'product': forms.Select(attrs={'class': 'text_inp', 'placeholder': 'Product'}),
            'user': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'User'}),
            'quantity': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'Quantity'}),
        }