from django import forms  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  
  
class SignupForm(UserCreationForm):  
    email = forms.EmailField(max_length=200, help_text='Required', required=True)
    first_name = forms.CharField(max_length=200, help_text='Required', required=True, min_length=3)
    last_name = forms.CharField(max_length=200, help_text='Required', required=True, min_length=5)  
    class Meta:  
        model = User  
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')  
