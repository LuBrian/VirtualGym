from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render,redirect

from django.http import HttpResponse
# from users.forms import SignUpForm
from django.contrib import auth
from django.contrib.auth import authenticate, login,logout
from users.models import MyUsers
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import json
from django.core.mail import EmailMessage
# import re

def signIn(request):
	"""
    Sign in the user through browser signIn page
    @type  instance: MyUser
    @param instance: The MyUser object
    """
	
	# get the input email and password from html page
	email = request.POST.get('email')
	password = request.POST.get('password')
	# check authentication on input email and password
	user = authenticate(request,email=email, password=password)

	# if user exists, log it in
	if user is None:
		print('user not exists')
		raise ValueError("Can't find user, please check again.")
	else:
		# print stuffs for back end check
		print("user exists")
		print(user.get_user_id())
		print(user.check_superuser() == True)
		login(request,user)
		return user

	# else give exception message, exception handlers
	# on Sign In and Sign Up will be done in next Sprint


def logOut(request):
	"""
	Log out the user.
	@type  request.User: Current authenticated User
	@param request.User: Current authenticated User
	"""
	logout(request)
	return redirect('index')
	# Redirect to a home page


@csrf_exempt 
def index(request):
	"""
	render for index.html, set page tite as home
	"""
	print('get called')
	title="Sign Up"
	exception = "None"
	# print('redner sign up form')
	# print(form)
	context={
		"title":title,
		"page_title":"Home",
		"exception": exception,
		"message": ""
	}
	# print('sending email')
	# email = EmailMessage('Subject', 'check email', to=['brianbylu@gmail.com'])
	# email.send()
	# print('finish send')
	if request.is_ajax():
		print("get post request")
		try:

			if(request.POST.get('formType') == "signIn"):
				validate_email(request.POST.get("email"))
				signInValidation(request.POST.get("password"))
				user = signIn(request)
				print('before return')
				return HttpResponse("ok")
				print("shouldn't be printed")

			elif(request.POST.get('formType') == "signUp"):
				print('sign up')
				validate_email(request.POST.get("email"))
				signUpValidation(request)
				username = clean_username(request.POST.get("username"))
				email = clean_email(request.POST.get("email"))
				instance = MyUsers.objects.create_user(username=username,
                                 email=email,
                                 password=request.POST.get("password"))

				user = authenticate(email=instance.email,password=instance.password)
				login(request, user)
				return HttpResponse("ok")
			else:
				print("shouldn't be printed")
		except Exception as e:
			print ('%s (%s)' % (e, type(e)))
			context["exception"] = e
			print(e[0])
			print('not valide')
			# print(context["exception"])
			# print(context)
			return HttpResponse(e[0])

	print('not ajax request')
	return render(
		request,
		'index.html',
		context,
	)









def signUpValidation(request):
	if request.POST.get('username') == "":
		print('empty username')
		raise ValueError("Enter a user name.")
	if request.POST.get('password') == "":
		print('empty password')
		raise ValueError("Enter a password.")
	if request.POST.get('confirm') == "":
		print('empty confirm')
		raise ValueError("Re-Enter the password.")
	if request.POST.get('confirm') != request.POST.get('password'):
		print('not match')
		raise ValueError("Passwords and confirmation not match.")
	

	
def signInValidation(password):
	print('signIn')
	print(password)
	if password == "":
		print('empty password')
		raise ValueError("Enter a password")



def clean_username(username):
	print(username)
	try:
		MyUsers._default_manager.get(username=username)
		#if the user exists, then let's raise an error message
		print("user already exists by username")
		raise ValueError('User name is already used, please use a new user name.')
	except MyUsers.DoesNotExist:
		return username # great, this user does not exist so we can continue the sign Up process


	

# exception handler on duplicate user email, will be completed in sprint 3
def clean_email(email):
	try:
		MyUsers._default_manager.get(email=email)
		print("user already exists by email")
		raise ValueError('Email is already used, please use a new email.')
	except MyUsers.DoesNotExist:
		return email # great, this user does not exist so we can continue the registration process

