from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Location

class UserRegestrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User

        fields = ['username','email','password1','password2']

class LocationRegestration(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['city','estate']

class UpdateLocation(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['city','estate']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User

        fields = ['username','email']    


class ProfileUpdateForm(forms.ModelForm):



    class Meta:
        model = Profile

        fields = ['image',]    
