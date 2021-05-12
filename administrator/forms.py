from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Mobile

class MobileCreateForm(ModelForm):
    class Meta:
     model=Mobile
     fields="__all__"
     # fields="__all__"

