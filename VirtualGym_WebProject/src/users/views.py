from django.http import HttpResponse


def signIn(request):
	template = loader.get_template('signIn.html')
	return HttpResponse(template.render())