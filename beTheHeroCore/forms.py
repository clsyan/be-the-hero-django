from beTheHeroCore.models import Account, Case
from django import forms
from django.contrib.auth.forms import UserCreationForm
from beTheHero import settings
from django.contrib.auth import models

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')


    class Meta:
        model = Account
        fields = ['location', 'email', 'username', 'password1', 'password2']

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = [
            'title',
            'description',
            'cost',
        ]
