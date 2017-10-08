from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
	user_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Sign Up Name'}))
	user_password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Input Passwrod'}))
	
	class Meta:
		model=SignUp
		fields={"user_name","user_password"}
