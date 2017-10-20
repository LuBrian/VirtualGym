from django import forms
from .models import MyUsers
# from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Sign Up Email'}))

	password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Input Passwrod'}))

	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User name'}))


	# exception = forms.CharField(
 #        label='exception',
 #        required=False,
 #        initial=False
 #     )

	class Meta:
		model= MyUsers
		fields={"email","password","username"}

	def clean_username(self):
		username = self.cleaned_data["username"]

		try:
			MyUsers._default_manager.get(username=username)
			#if the user exists, then let's raise an error message
			print("user already exists")
			raise forms.ValidationError('Username is already in use.')
		except MyUsers.DoesNotExist:
			return username # great, this user does not exist so we can continue the registration process
	
		


	# def clean_email(self):
	# 	email = self.cleaned_data["email"]
	# 	try:
	# 		MyUsers._default_manager.get(email=email)
	# 		#if the user exists, then let's raise an error message
	# 		print("user already exists")
	# 		# raise forms.ValidationError( 
	# 		# 	self.exception['duplicate_username']
	# 			# print('user exists')  #user my customized error message

	# 		# code='duplicate_username',   #set the error message key

	# 	# )
	# 	except MyUsers.DoesNotExist:
	# 		return email # great, this user does not exist so we can continue the registration process


