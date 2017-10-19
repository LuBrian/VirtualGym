from django.shortcuts import render

# Create your views here.
from .forms import QuestionsForm
from .models import Questions
from users.models import MyUsers

def CreateQuestion(request):
    quearyset=Questions.objects.all()
    title=" Create Your Questions"
    form= QuestionsForm(request.POST or None)
    context={
		"form":form,
        "title":title,
        "objects_list":quearyset,
	}
    if form.is_valid():
        instance=form.save(commit=False)
        instance.userID= request.user
        instance.save()
        context={
            "form":"",
            "objects_list":quearyset,
        }


    return render(request,"QA.html",context)
    # return render(request,"questionPos.html",context)
