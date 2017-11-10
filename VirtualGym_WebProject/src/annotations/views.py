# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from exercise.models import Videos
# from .forms import AnnotationForm
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.http import HttpResponse,JsonResponse
from .models import Annotation
import json
# Create your views here.

@csrf_exempt #This skips csrf validation. Use csrf_protect to have validation
def createAnnotation(request,vidID):


	instance=get_object_or_404(Videos,video_id=vidID)
	title="Add annotations"

	annotationSet = Annotation.objects.filter(toVid=vidID)
	dataSet = []
	for element in annotationSet:
		dataSet.append(element.details);
	json_string = json.dumps(dataSet)
	
	


	if request.is_ajax():
		print('in ajax')
		if request.method == "POST":
			print("in post ajax")
			print('in ajax')
			JSONdata = request.body
			tempAnnotation = Annotation(toVid=instance, details=JSONdata)
			tempAnnotation.save()
			return HttpResponse("OK")

		if request.method == "GET":
			print('in get ajax')

			return HttpResponse(json_string)

	context = {
		"title":title,
		"instance":instance,
		"contents" :json_string,
	}
	

	return render(request,"addAnnotation.html",context)
