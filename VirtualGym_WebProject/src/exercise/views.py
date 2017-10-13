from django.shortcuts import render,get_object_or_404

from .forms import CreateExeForm
from .models import Exercise

from .models import Exercise
from .models import Videos
from .models import VideosExercises
from .models import Tags
from .models import TagsExercises

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
		data=form.cleaned_data
		
		createVideo(data,instance)
		addTagsToDB(data["exerciseTag"],instance)
		context={
			"title":"Thank You"
		}
		# print (instance.user_name)
		# print (instance.user_id)

	return render(request,"createExercise.html",context)

def Profile(request):
	title=" Profile of Exercise "
	quearyset=Exercise.objects.all()

	context={
		"title":title,
		"objects_list":quearyset
	}
	return render(request,"viewProfile.html",context)

def Exercise_detail(request,id=None):
	title=" Detail of Exercise "
	instance=get_object_or_404(Exercise,exerciseId=id)
	context={
		"title":title,
		"instance":instance,
	}
	return render(request,"detail.html",context)





def createVideo(data, exerciseObj):
	videoName = data['exerciseVideos']
	videos_obj = Videos(videoFile=videoName,exercisePosterId= exerciseObj.exercisePosterId)
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
