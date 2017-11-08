from django import forms
from .models import MyUsers




"""/******************************
** File: forms.py   
** Desc: This file interacts with the MyUser model and given Sign Up forms in HTML
** Currently, Creating an New User when sign up is processed
*******************************/"""

class SignUpForm(forms.ModelForm):
	# html email input content
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Sign Up Email'}))
	# html password input box
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Input Password'}))
	# html password confirm box
	confirm = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
	# html username input box
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User name'}))

	class Meta:
		model= MyUsers
		fields={"email","password","username", "confirm"}


	# exception handler on duplicate user name, will be completed in sprint 3
	def clean_username(self):
		username = self.cleaned_data["username"]

		try:
			MyUsers._default_manager.get(username=username)
			#if the user exists, then let's raise an error message
			print("user already exists by username")
			raise ValueError('User name is already used, please user a new user name')
		except MyUsers.DoesNotExist:
			return username # great, this user does not exist so we can continue the sign Up process
	
	#exception handler on password confirmation
	def clean(self):
		super(SignUpForm, self).clean()
		password = self.cleaned_data["password"]
		confirm = self.cleaned_data["confirm"]
		if password != confirm:
			msg ="Passwords do not match"
			print(msg)
			self.add_error('password', msg)
			self.add_error('confirm', msg)
			raise forms.ValidationError(msg)
		

	# exception handler on duplicate user email, will be completed in sprint 3
	def clean_email(self):
		email = self.cleaned_data["email"]
		try:
			MyUsers._default_manager.get(email=email)
			print("user already exists by email")
			raise ValueError('User email is already used, please user a new user email')
		except MyUsers.DoesNotExist:
			return email # great, this user does not exist so we can continue the registration process


