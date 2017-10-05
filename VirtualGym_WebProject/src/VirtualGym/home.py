from django.http import HttpResponse
from django.template import loader

def index(request):
	template = loader.get_template('index.html')
	return HttpResponse(template.render())




def signIn(request):
	signinTemp = loader.get_template('signIn.html')
	print("signin page")
	return HttpResponse(signinTemp.render())