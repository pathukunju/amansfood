from django import forms
from .models import Order
from django.contrib.auth.models import User



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name','email','phone']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    # password2 = forms.CharField(widget=forms.PasswordInput)
    mobile = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username','email']