from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib import auth
from django.contrib.auth import authenticate, login,logout
from .models import MyUsers
# from django.contrib.auth.models import MyUsers
# from users.models import MyUsers

"""/******************************
** File: views.py   
** Desc: This file is used as a controller to interact with the front-end and back-end of the virtual gym's customer user model.
** For example, New User email sign up, User sign in, social media sign in like
facebook, twitter and google.
*******************************/"""




def signIn(request):
	"""
    Sign in the user through browser signIn page
    @type  instance: MyUser
    @param instance: The MyUser object
    """
	
	title="Sign In"
	# get the input email and password from html page
	email = request.POST.get('email')
	password = request.POST.get('password')
	# check authentication on input email and password
	user = authenticate(request,email=email, password=password)

	# if user exists, log it in
	if user is not None:
		# print stuffs for back end check
		print("user exists")
		print(user.get_user_id())
		print(user.check_superuser() == True)
		login(request,user)
		return redirect('index')

	# else give exception message, exception handlers
	# on Sign In and Sign Up will be done in next Sprint
	else:
		print(user)
		print('user not exists')
	return render(
        request,
        'signIn.html',
        {'title':title},
        user
    )


def signUp(request):
	"""
    creater new MyUsers according user input and translate to database.
    @type  instance: MyUser object
    @param instance: The MyUser which will be created here and authenticated
    right after signed up.
    """
	title="Sign Up"
	form= SignUpForm(request.POST or None)
	exception = "None"
	

	context={
		"title":title,
		"form":form,
		"page_title":title,
		"exception": exception
	}
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		user = authenticate(email=instance.email,password=instance.password)
		login(request, user)
		return redirect('index')


	return render(request,"signUp.html",context)
		


	

	

def logOut(request):
	"""
	Log out the user.
	@type  request.User: Current authenticated User
	@param request.User: Current authenticated User
	"""
	logout(request)
	return redirect('index')
	# Redirect to a home page




