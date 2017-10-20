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
	"""
    creater exercise according user input and translate to database.
    @type  instance: exercise
    @param instance: The exercise object.
    """
	title=" Create Your Exercise"
	form= CreateExeForm(request.POST or None,request.FILES)
	context={
		"title":title,
		"form":form,
	}

	if form.is_valid():
		instance=form.save(commit=False)
		instance.exercisePosterId= request.user
		instance.save()
		data=form.cleaned_data

		createVideo(data,instance)
		addTagsToDB(data["exerciseTag"],instance)
		addTagsToDB(data["exTag"].split(","), instance)
		context={
			"title":"Thank You"
		}
		return HttpResponseRedirect('/myExercise/')

	return render(request,"createExercise.html",context)

def Profile(request):
	"""
    get all approved exercise from server and return to view all exercise page by context.
    @type  quearyset: set of exercise
    @param quearyset: The set of all approved exercise object.
    """
	title=" Profile of Exercise "
	quearyset=Exercise.objects.filter(exerciseApproved = True)

	context={
		"title":title,
		"objects_list":quearyset
	}
	return render(request,"viewProfile.html",context)


def MyExercise(request):
	"""
    get exercise list from server according user and return to my exercise page by context.
    @type  quearyset: set of exercise
    @param quearyset: The set of all my exercise object.
    """
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
			"objects_list":quearyset,
		}
	return render(request,"myExercise.html",context)




def Exercise_detail(request,id=None):
	"""
    1.view each exercise according exercise Id(return to my exercise page by context).
	2.receiving fron end comment and translate to database.
    @type  instance: exercise id
    @param instance: view exercise detail according exercise Id.

    @type  comment_form: string
    @param comment_form: front end comment input string.

    @type  obj_content: comment object .
    @param obj_content: get comment descriptin put in obj_content.

    @type  parent_obj: parent comment object.
    @param parent_obj: if one comment do not have parent, then parent is None.

    @type  parent_id:  int.
    @param parent_id: get parent id from front end if current object is reply.

    @type  parent_qs: parent comment object list .
    @param parent_qs: get reply's parent according parent id,if have parent then set parent_obj.

    @type  new_comment: new comment object.
    @param obj_content: new a comment object and save it to database.
    """

	title=" Detail of Exercise "
	instance=get_object_or_404(Exercise,exerciseId=id)

	comment_form=CommentForm(request.POST or None)
	if comment_form.is_valid():

		obj_content=comment_form.cleaned_data.get("comment")
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
