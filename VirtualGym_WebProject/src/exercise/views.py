from django.shortcuts import render

import models
from .forms import CreateExeForm
from .models import Exercise
from .models import Videos
from .models import VideosExercises
from .models import Tags
from .models import TagsExercises
from .videoEnums import VideoPerspective
from users.models import MyUsers

def CreateExe(request):
	title=" Create Your Exercise"
	form= CreateExeForm(request.POST or None,request.FILES)
	context={
		"title":title,
		"form":form,
	}
	if form.is_valid():
		instance=form.save(commit=False)
		instance.exercisePosterId= request.user
		# instance.exercisePosterId= MyUsers.objects.create(username ="Lvxin",password="234");
        #print (instance.exerciseTag)
		instance.save()
		data = form.cleaned_data
		createVideos(data, instance)
		myListOfTags = data['exTag'].split(",")
		addTagsToDB(myListOfTags, instance)
		context={
			"title":"Thank You"
		}

		# print (instance.user_name)
		# print (instance.user_id)

	return render(request,"createExercise.html",context)

def createVideos(data, exerciseObj):
	topVideo = data['topVideo']
	backVideo = data['backVideo']
	frontVideo = data['frontVideo']
	leftVideo = data['leftVideo']
	rightVideo = data['rightVideo']
	threeQuartersVideo = data['threeQuartersVideo']

	if topVideo is not None:
		createVideo(topVideo, exerciseObj, VideoPerspective.TOP)
	if leftVideo is not None:
		createVideo(leftVideo, exerciseObj, VideoPerspective.LEFT)
	if rightVideo is not None:
		createVideo(rightVideo, exerciseObj, VideoPerspective.RIGHT)
	if frontVideo is not None:
		createVideo(frontVideo, exerciseObj, VideoPerspective.FRONT)
	if backVideo is not None:
		createVideo(backVideo, exerciseObj, VideoPerspective.BACK)
	if threeQuartersVideo is not None:
		createVideo(threeQuartersVideo, exerciseObj, VideoPerspective.THREEQUARTERS)
		
def createVideo(videoName, exerciseObj, videoPerspec):
	videos_obj = Videos(videoFile=videoName, videoPerspective = videoPerspec.value)
	videos_obj.save()
	
	createVideoExerciseRelationship(videos_obj, exerciseObj)

def createVideoExerciseRelationship(videoID, exerciseObj):
	videosExercises_obj = VideosExercises(video_id = videoID, exercise_id = exerciseObj)
	videosExercises_obj.save()

def addTagsToDB(listOfTags, exerciseObj):
	for tag in listOfTags:
		createTag(tag, exerciseObj)

def createTag(tag, exerciseObj):
	tag_obj = Tags()
	if not Tags.objects.filter(tagDescription=tag).exists():
		tag_obj = Tags(tagDescription = tag)
		tag_obj.save()
	else:
		tag_obj = Tags.objects.get(tagDescription=tag)
	
	createTagRelationship(tag_obj, exerciseObj)

def createTagRelationship(tag_obj, exerciseObj):
	tagRelationshipObj = TagsExercises(tag_id = tag_obj, exercise_id = exerciseObj)
	tagRelationshipObj.save()
	
