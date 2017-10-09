from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib import auth
from django.contrib.auth import authenticate, login,logout




def signIn(request):
	title="Sign In"
	email = request.POST.get('email')
	password = request.POST.get('password')
	# usr = MyUsers.objects.get(user_name='username')
	# print(usr)
	user = authenticate(request,email=email, password=password)
	# print(password)
	# print(username)
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
	context={
		"title":title,
		"form":form,
		"page_title":title
	}
	if form.is_valid():
		
		instance=form.save(commit=False)
		# instance.is_superuser = True
		# print(form.email)
		instance.username = instance.email
		instance.save()
		login(request, instance)
		return redirect('index')
		# print (instance.user_name)
		# print (instance.user_id)
	else:
		print("not signed up")

	return render(request,"signUp.html",context)
	#template = loader.get_template('signIn.html')
	#return HttpResponse(template.render())

def logOut(request):
    logout(request)
    return redirect('index')
    # Redirect to a succes
