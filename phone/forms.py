from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms 
from django.forms import ModelForm 
from .models import Payno

class ProductForm(ModelForm):
    class Meta:
        model=Payno
        fields=['name_in_card','number_card','date_card','cvv_card']

        labels={
            'name_in_card':'Enter Name same in Carde',
            'number_card':'Enter Number',
            'date_card':'Enter Date',
            'cvv_card':'Enter CVV',
 
        }
        widgets={
            'name_in_card':forms.TextInput(attrs={'class':'form-control form-control-sm text-success'}),
            'number_card':forms.TextInput(attrs={'class':'form-control text-success'}),
            'date_card':forms.TextInput(attrs={'class':'form-control text-success'}),
            'cvv_card':forms.TextInput(attrs={'class':'form-control text-success'}),
        }



class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')

class LoginUserForm(AuthenticationForm):
    class Meta:
        model=User
        fields={'username','password'}