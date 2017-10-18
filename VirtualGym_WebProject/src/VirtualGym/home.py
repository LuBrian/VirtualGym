from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render


def home(request):
    return render_to_response('home.html')

def index(request):
	#template = loader.get_template('index.html')
	return render(
        request,
        'index.html',
        {'page_title':"Home"},
    )





