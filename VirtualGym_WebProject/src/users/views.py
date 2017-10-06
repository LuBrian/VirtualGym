from django.http import HttpResponse
from django.shortcuts import render
from .forms import SignUpForm

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
		instance.save()
		context={
			"title":"Thank You",
		}
		# print (instance.user_name)
		# print (instance.user_id)

	return render(request,"signUp.html",context)
	#template = loader.get_template('signIn.html')
	#return HttpResponse(template.render())
