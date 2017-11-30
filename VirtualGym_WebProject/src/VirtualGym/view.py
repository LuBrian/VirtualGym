from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render,redirect

from django.http import HttpResponse
from users.forms import SignUpForm
from django.contrib import auth
from django.contrib.auth import authenticate, login,logout
from users.models import MyUsers




def index(request):
	"""
	render for index.html, set page tite as home
	"""

	title="Sign Up"
	form= SignUpForm(request.POST or None)
	exception = "None"
	print('redner sign up form')
	# print(form)
	context={
		"title":title,
		"form":form,
		"page_title":"Home",
		"exception": exception
	}

	if request.method == 'POST':
		try:
			form.is_valid()
			instance=form.save(commit=False)
			instance.save()
			user = authenticate(email=instance.email,password=instance.password)
			login(request, user)
			return redirect('index')
		except Exception as e:
			print ('%s (%s)' % (e, type(e)))
			context["exception"] = e
			# print(context["exception"])
			# print(context)
		
		return render(request,"index.html",context)

		
	return render(
		request,
		'index.html',
		context,
	)





def clean_username(self):
	username = self.cleaned_data["username"]
	print(username)
	try:
		MyUsers._default_manager.get(username=username)
		#if the user exists, then let's raise an error message
		print("user already exists by username")
		raise ValueError('User name is already used, please use a new user name')
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
		raise ValueError(msg)
	

# exception handler on duplicate user email, will be completed in sprint 3
def clean_email(self):
	email = self.cleaned_data["email"]
	try:
		MyUsers._default_manager.get(email=email)
		print("user already exists by email")
		raise ValueError('User email is already used, please use a new user email')
	except MyUsers.DoesNotExist:
		return email # great, this user does not exist so we can continue the registration process