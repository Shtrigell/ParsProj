from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import AuthenticationForm

class AddUrlForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':10}), label='Ссылка')

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta():
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class':'form-input'}))



class HistoryForm(forms.Form):
    class Meta():
        model = History
        fields = '__all__'


    
