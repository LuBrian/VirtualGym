from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import QuestionsForm
from .models import Questions
from users.models import MyUsers

def CreateQuestion(request):
    """
    1.view all question (return to my QA page by context).
    2.receiving fron end answer and translate to database.
    @type  quearyset: question objects.
    @param quearyset: list of question object..

    @type  form: string
    @param form: front end question input string.

    @type  instance: question object .
    @param instance: question object for save in database.

    @type  parent_obj: parent comment object.
    @param parent_obj: if one comment do not have parent, then parent is None.

    @type  parent_id:  int.
    @param parent_id: get parent id from front end if current object is an answer.

    @type  parent_qs: parent question object list .
    @param parent_qs: get answer's parent according parent id,if have parent then set parent_obj.

    """
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
