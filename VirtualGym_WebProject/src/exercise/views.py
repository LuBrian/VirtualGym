from django.shortcuts import render

from .forms import CreateExeForm
from .models import Exercise
from users.models import MyUsers

def CreateExe(request):
	title=" Create Your Exercise"
	form= CreateExeForm(request.POST or None,request.FILES)
	context={
		"title":title,
		"form":form,
	}
	if form.is_valid():
		instance=form.save(commit=False)
		instance.exercisePosterId=MyUsers.objects.create(user_name ="Lvxin",user_password="234");
        #print (instance.exerciseTag)
		instance.save()

		context={
			"title":"Thank You"
		}
		# print (instance.user_name)
		# print (instance.user_id)

	return render(request,"createExercise.html",context)
