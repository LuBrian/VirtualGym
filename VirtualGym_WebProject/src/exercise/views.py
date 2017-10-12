from django.shortcuts import render,get_object_or_404

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
		instance.exercisePosterId= request.user
		# instance.exercisePosterId= MyUsers.objects.create(username ="Lvxin",password="234");
        #print (instance.exerciseTag)
		instance.save()

		context={
			"title":"Thank You"
		}
		# print (instance.user_name)
		# print (instance.user_id)

	return render(request,"createExercise.html",context)

def Profile(request):
	title=" Profile of Exercise "
	quearyset=Exercise.objects.all()
	print(quearyset)
	context={
		"title":title,
		"objects_list":quearyset
	}

	return render(request,"viewProfile.html",context)

def Exercise_detail(request,id=None):
	title=" Detail of Exercise "
	instance=get_object_or_404(Exercise,exerciseId=id)
	context={
		"title":title,
		"instance":instance,
	}
	return render(request,"detail.html",context)
