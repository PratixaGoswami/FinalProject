from django import forms
from .models import *

class usersignupform(forms.ModelForm):
    class Meta:
        model=usersignup
        fields='__all__'

class noteform(forms.ModelForm):
    class Meta:
        model=mynotes
        fields="__all__"

class contactform(forms.ModelForm):
    class Meta:
        model=contactus
        fields="__all__"        
