from .models import UserC
from django import forms
from django.contrib.auth.models import User

class ChangeUser(forms.ModelForm):
   class Meta:
        model = UserC
        fields = ['first_name', 'last_name', 'email', 'phone', 'avatar']
        exlide = ['auth_user']