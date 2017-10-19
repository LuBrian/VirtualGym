from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect

from comments.forms import CommentForm
from .forms import CreateExeForm
from .models import Exercise

from .models import Videos
from .models import VideosExercises
from .models import Tags
from .models import TagsExercises

from users.models import MyUsers
from comments.models import Comment

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
		addTagsToDB(data["exTag"].split(","), instance)
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


def MyExercise(request):
	title=" My Exercise "
	try:
		quearyset=Exercise.objects.filter(exercisePosterId = request.user)
		context={
			"title":title,			
			"objects_list":quearyset
		}
	except:
		quearyset = []
		context={
			"title":title,			
			"objects_list":quearyset
		}
	return render(request,"MyExercise.html",context)




def Exercise_detail(request,id=None):

	title=" Detail of Exercise "
	instance=get_object_or_404(Exercise,exerciseId=id)

	comment_form=CommentForm(request.POST or None)
	if comment_form.is_valid():
		print(comment_form.cleaned_data)

		obj_content=comment_form.cleaned_data.get("content")
		parent_obj=None;
		try:
			parent_id=int(request.POST.get("parent_id"))
		except:
			parent_id=None

		if parent_id:
			parent_qs=Comment.objects.filter(CommentId=parent_id)
			if parent_qs.exists() and parent_qs.count()==1:
				parent_obj=parent_qs.first()
		new_comment=Comment(
					CommentPoster=request.user,
					CommentExercise=instance,
					CommentContent=obj_content,
					CommentParent=parent_obj,
		)
		new_comment.save();
		return HttpResponseRedirect(new_comment.CommentExercise.get_absolute_url())

	context={
		"title":title,
		"instance":instance,
		"comment_form":comment_form,
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
	print(listOfTags)
	for tag in listOfTags:
		createTag(tag, exerciseObj)

def createTag(tag, exerciseObj):
	print(tag)
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
