from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    email = forms.EmailField(max_length=254,  widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    password1 = forms.CharField(max_length=20,label="Password", widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'8+ characters'}))
    password2 = forms.CharField(max_length=20,label="Confirm Password", widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}))
    
    
    
    class Meta:
        model = User
        fields = ['username', 'first_name',  'email', 'password1', 'password2']