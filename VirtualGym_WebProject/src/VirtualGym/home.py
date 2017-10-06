from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

def index(request):
	#template = loader.get_template('index.html')
	return render(
        request,
        'index.html',
        {'page_title':"Home"},
    )




def signIn(request):
	# return HttpResponse(signinTemp.render())
	return render(
        request,
        'signIn.html',
        {'page_title':"Sign In"},
    )


def signUp(request):

	return render(
        request,
        'SignUp.html',
        {'page_title':"Sign Up"},
    )
