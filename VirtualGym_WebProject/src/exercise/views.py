from django.shortcuts import render

from .forms import CreateExeForm

def CreateExe(request):
	title=" Create Your Exe"
	form= CreateExeForm(request.POST or None)
	context={
		"title":title,
		"form":form
	}

	if form.is_valid():
		instance=form.save(commit=False)
        #print (instance.exerciseTag)
		instance.save()

		context={
			"title":"Thank You"
		}
		# print (instance.user_name)
		# print (instance.user_id)

	return render(request,"createExercise.html",context)
