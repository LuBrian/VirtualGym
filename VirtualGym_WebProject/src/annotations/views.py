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
	"""
	After create the exercise, create annotation when click on a video
	@type  vidID: vidID, int
    @param vidID: passed in vidID
    @type  instance: video
    @param instance: video instance find by vidID
    @type  annotationSet: list
    @param annotationSet: list stores this instance's annotations
    @type  json_string: string
    @param json_string: json string contains this video's annotations
	"""

	instance=get_object_or_404(Videos,video_id=vidID)
	title="Add annotations"

	annotationSet = Annotation.objects.filter(toVid=vidID)
	dataSet = []
	for element in annotationSet:
		dataSet.append(element.details);
	json_string = json.dumps(dataSet)
	
	

	# if it is a ajax post or get request,create a new annotation or send the updated annotations json string
	if request.is_ajax():
		if request.method == "POST":
			JSONdata = request.body
			tempAnnotation = Annotation(toVid=instance, details=JSONdata)
			tempAnnotation.save()
			return HttpResponse("OK")

		if request.method == "GET":

			return HttpResponse(json_string)

	context = {
		"title":title,
		"instance":instance,
		"contents" :json_string,
	}
	

	return render(request,"addAnnotation.html",context)
