from django.shortcuts import render

from .models import Exercise

def Profile(request):
	title=" Profile of Exercise "
	quearyset=Exercise.objects.all()
	print(quearyset)
	context={
		"title":title,
		"objects_list":quearyset
	}
	return render(request,"viewProfile.html",context)
