from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import QuestionsForm
from .models import Question
from users.models import MyUsers

def CreateQuestion(request):
    """
    1.view all question (return to my QA page by context).
    2.allow admin add FAQ question end answer.
    @type  quearyset: question objects.
    @param quearyset: list of question object..

    @type  form: string
    @param form: front end question input string.


    """
    quearyset=Question.objects.all()
    title="Frequently Asked Questions"
    form= QuestionsForm(request.POST or None)
    print(quearyset)
    context={
    	"form":form,
        "title":title,
        "objects_list":quearyset,
    }

    return render(request,"QA.html",context)
