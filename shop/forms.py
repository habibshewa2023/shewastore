from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your firstname'})
    )
    
    last_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your lastname'})
    )
    
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your email'})
    )
    
    username = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your username'})
    )
    
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'name':'password',
                'type':'password',
                'placeholder':'Enter your password'
            }
        )
    )
    
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'name':'password',
                'type':'password',
                'placeholder':'Confirm password'
            }
        )
    )
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','username','password1','password2')
        
        
class UpdateUserForm(UserChangeForm):
    password = None
    first_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your firstname'})
        ,required=False
    )
    
    last_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your lastname'})
        ,required=False
    )
    
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your email'})
        ,required=False
    )
    
    username = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your username'})
        ,required=False
    )
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name','email','username')
        
class UpdatePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'name':'password',
                'type':'password',
                'placeholder':'Enter your new password'
            }
        )
    )
    
    new_password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'name':'password',
                'type':'password',
                'placeholder':'Confirm password'
            }
        )
    )
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']
        
class UpdateUserInfo(forms.ModelForm):
    phone = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your phone'})
        ,required=False
    )
    address1 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your address 1'})
        ,required=False
    )
    address2 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your address 2'})
        ,required=False
    )
    province = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your province'})
        ,required=False
    )
    city = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your city'})
        ,required=False
    )
    state = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your state'})
        ,required=False
    )
    
    class Meta:
        model = Profile
        fields = ('phone', 'address1', 'address2', 'province', 'city', 'state')