from django import forms
from .models import *

class user_form(forms.Form):
    roll_number=forms.IntegerField()
    name=forms.CharField()
    age=forms.IntegerField()
    email=forms.EmailField()



class model_form(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'