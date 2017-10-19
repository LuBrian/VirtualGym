from django.shortcuts import render
from django.http import HttpResponseRedirect

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
        parent_obj=None;
        try:
            parent_id=int(request.POST.get("questionparent_id"))
        except:
            parent_id=None

        if parent_id:
            parent_qs=Questions.objects.filter(questionID=parent_id)
            if parent_qs.exists() and parent_qs.count()==1:
                parent_obj=parent_qs.first()
        instance.questionParent=parent_obj
        instance.save()

        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request,"QA.html",context)
    # return render(request,"questionPos.html",context)
