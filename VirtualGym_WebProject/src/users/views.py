from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib import auth
from django.contrib.auth import authenticate, login,logout
from .models import MyUsers
# from django.contrib.auth.models import MyUsers
# from users.models import MyUsers



def signIn(request):
	title="Sign In"
	email = request.POST.get('email')
	password = request.POST.get('password')
	# usr = MyUsers.objects.get(user_name='username')
	# print(usr)

	user = authenticate(request,email=email, password=password)
	print(password)
	print(email)

	if user is not None:
		print("user exists")
		print(user.get_user_id())
		print(user.check_superuser() == True)
		login(request,user)
		return redirect('index')

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
	title="Sign Up"
	form= SignUpForm(request.POST or None)
	exception = "None"
	
	# try:
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
		

	# except:
	# 	print("signup exception")
	# 	context["exception"] = "User name has been taken"

	# 	return render(request,"signUp.html",context)

	

	

def logOut(request):
    logout(request)
    return redirect('index')
    # Redirect to a succes
