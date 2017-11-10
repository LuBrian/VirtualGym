# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from exercise.models import Videos
# from .forms import AnnotationForm
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.http import HttpResponse
from .models import Annotation
import json
# Create your views here.

@csrf_exempt #This skips csrf validation. Use csrf_protect to have validation
def createAnnotation(request,vidID):
	print('haha')

	instance=get_object_or_404(Videos,video_id=vidID)
	title="Add annotations"

	
	print('before post')

	if request.is_ajax():
		print('in ajax')
		JSONdata = request.body
		# tempDict = simplejson.JSONDecoder().decode( JSONdata ) 
		data_dict = json.loads(JSONdata)[0]
		tempAnnotation = Annotation(toVid=instance, details=data_dict["details"], x = data_dict["x"],y=data_dict["y"],timeStep = data_dict["time"])
		tempAnnotation.save()
		return HttpResponse("OK")


	context = {
		"title":title,
		"instance":instance,
	}

	return render(request,"addAnnotation.html",context)
