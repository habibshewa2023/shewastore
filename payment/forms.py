from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your Fullname'})
        ,required=True
    )
    
    shipping_email = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your Email'})
        ,required=True
    )
    
    shipping_phone = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your Phone'})
        ,required=True
    )
    
    shipping_address1 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your address 1'})
        ,required=True
    )
    shipping_address2 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your address 2'})
        ,required=False
    )
    shipping_province = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your province', 'value':'Afghanistan'})
        ,required=True
    )
    shipping_city = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your city'})
        ,required=True
    )
    shipping_state = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your state'})
        ,required=True
    )
    
    class Meta:
        model = ShippingAddress
        fields = [
            'shipping_full_name',
            'shipping_email',
            'shipping_phone',
            'shipping_address1',
            'shipping_address2',
            'shipping_province',
            'shipping_city',
            'shipping_state'
        ]
        
        exclude = ['user',]