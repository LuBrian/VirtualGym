from django import forms
from .models import MyUsers
# from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Sign Up Email'}))

	password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Input Passwrod'}))

	class Meta:
		model= MyUsers
		fields={"email","password"}
