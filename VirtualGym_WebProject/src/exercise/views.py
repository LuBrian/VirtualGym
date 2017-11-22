from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from django.db.models import Q
from comments.forms import CommentForm
from .forms import CreateExeForm
from .forms import EditExeForm

from .models import Exercise,Tags,TagsExercises
from .forms import TAG_CHOICE


from .models import Videos
from .models import VideosExercises
from .models import Tags
from .models import TagsExercises

from users.models import MyUsers
from comments.models import Comment
import re,json
from django.views.decorators.csrf import csrf_exempt
"""/******************************
** File: views.py
** Desc: This file is used as a controller to interact with the front-end and back-end of the given exercises app.
** For example, Create Exercise, View Exercises, and My Exercise are all formed through here.
*******************************/"""
@csrf_exempt #This skips csrf validation. Use csrf_protect to have validation
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
		print('form submit')
		instance=form.save(commit=False)
		instance.exercisePosterId= request.user
		instance.save()
		data=form.cleaned_data

		jsonData = request.POST.get('returnData').split("||")

		createVideos(data,instance,jsonData)
		addTagsToDB(data["exerciseTag"],instance)
		addTagsToDB(data["exTag"].split(","), instance)
		context={
			"title":"Thank You"
		}

		return HttpResponseRedirect('/myExercise/')
		# return redirect('annotations',vidID = vidid)

	return render(request,"createExercise.html",context)

def Profile(request):
	"""
    1.get all approved exercise from server and return to view all exercise page by context.
	2.filter exercise by tag and descriptin var search file.

    @type  quearyset: set of exercise
    @param quearyset: The set of all approved exercise object. if front end send search request,
						filter exercise according request.

    @type  queary: string
    @param queary: request string from front end.

    """
	title=" Profile of Exercise "
	quearyset=Exercise.objects.filter(exerciseApproved = True)
	query=request.GET.get("q")


	if query:
		queryList = re.split(' |,',query)
		for i in queryList:
			quearyset=quearyset.filter(
				Q(exerciseDescription__icontains = i) |
				Q(exerciseTag__tagDescription__icontains = i)
			).distinct()

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
	3.filter database according the same tag and show in front as cross referance.

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
    @param new_comment: new a comment object and save it to database.

    @type  quearyset: set.
    @param quearyset: set of exercise object with same tag.

    @type  taglist: tag object.
    @param taglist: list of tag.
    """

	title=" Detail of Exercise "
	instance=get_object_or_404(Exercise,exerciseId=id)
	comment_form=CommentForm(request.POST or None)

	quearyset=[]
	taglist=instance.exerciseTag.all()
	quearyset=getExebytag(taglist)

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
		"quearyset":quearyset,
	}
	return render(request,"detail.html",context)

def getExebytag(taglist):
	"""
	1.according the tag list return exercises with same tag
    @type  quearyset: set.
    @param quearyset: set of exercise object with same tag.

    @type  tagset: tag object.
    @param tagset: list of tag.
    """
	quearyset=[]
	tagset=[]
	for tag in taglist:
		if tag.tagDescription not in [None, '']:
			print(tag.tagDescription)
			tagset=Exercise.objects.filter(
				Q(exerciseApproved = True) &
				Q(exerciseTag__tagDescription = tag)).distinct()
			for i in tagset:
				if i not in quearyset:
					quearyset.append(i)
	return quearyset

def getTags(exTags):
	"""
	1.tostring method for tags.

    """
	tags = ""
	for tag in exTags:
		tags = tags+", "+str(tag)
	return tags[2:]

def EditExe(request,id=None):
	"""
	1.according the current exercises edit descriptin, tags.

    @type  instance: exercise object.
    @param instance: exercise object according by current user click exercise.

    @type  form: edit form.
    @param form: provide a form interact between front and back to save edit.

    """

	instance=get_object_or_404(Exercise,exerciseId=id)
	vid_instances = instance.exerciseVideos.all()
	# vid_instances = VideosExercises.objects.filter(exercise_id = id)
	# print(vid_instances)
	videos = []
	for element in vid_instances:
		videos.append(element)

		# print element.videoFile.url

	form= EditExeForm(request.POST or None,instance=instance, initial={"exerciseTag": getTags(instance.exerciseTag.all())})
	if form.is_valid():
		instance=form.save(commit=False)
		instance.exerciseApproved=False
		instance.exerciseTag.clear()

		data=form.cleaned_data
		addTagsToDB(data["exerciseTag"].split(","), instance)

		instance.save()
		if request.method == "POST":
			jsonData = request.POST.get('returnData')
			annotaiton_data = json.loads(jsonData)
			set_video_annotation(annotaiton_data)


		return HttpResponseRedirect('/myExercise/')
	context={
	"title":"Edit Exercist",
	"instance":instance,
	"form":form,
	"videos": json.dumps(videos_to_dict(videos))
	}
	return render(request,"edit.html",context)

def set_video_annotation(myData):
	print('before set annotation')
	print(myData)
	for element in myData:

		item = get_object_or_404(Videos,video_id=element["video_id"])
		print(item)
		print(item.annotations)
		item.annotations = element["annotations"]
		item.save()

def videos_to_dict(myVids):
	vidList = []
	for item in myVids:
		vidList.append({"video_id": item.video_id, "annotations": item.annotations,"url":item.videoFile.url })
	print(vidList)
	return vidList


def createVideos(data, exerciseObj, jsonData):
	ex1 = data['exerciseVideos1']
	ex2 = data['exerciseVideos2']
	ex3 = data['exerciseVideos3']
	ex4 = data['exerciseVideos4']
	ex5 = data['exerciseVideos5']

	if ex1 is not None:
		createVideo(ex1, exerciseObj, jsonData[0])
	if ex2 is not None:
		createVideo(ex2, exerciseObj, jsonData[1])
	if ex3 is not None:
		createVideo(ex3, exerciseObj, jsonData[2])
	if ex4 is not None:
		createVideo(ex4, exerciseObj, jsonData[3])
	if ex5 is not None:
		createVideo(ex5, exerciseObj, jsonData[4])

def createVideo(videoName, exerciseObj,jsonData):
	"""createVideo

	This subroutine creates a video object from the file uploaded and calls createVideoExerciseRelationship to form the relationship in the normalized table.
	Args:
	data: An instance of well-formatted clean output from the form,
	exerciseObj: An exercise instance attached to the newly created exercise object(which is formed in the createExercise screen)

	Returns:
	Nothing

	"""
	print(videoName)
	print(jsonData)
	videos_obj = Videos(videoFile=videoName,exercisePosterId= exerciseObj.exercisePosterId,annotations = jsonData)
	videos_obj.save()

	createVideoExerciseRelationship(videos_obj, exerciseObj)
	return videos_obj.video_id

def createVideoExerciseRelationship(videoID, exerciseObj):
	"""createVideoExerciseRelationship

	This subroutine creates a VideoExercises object (a normalized table used to store relationships of exercises to videos)
	Args:
	videoID : An instance of the Video object.
	exerciseObj: An instance of the newly created exercise object from Create Exercise.

	Returns:
	Nothing

	"""
	videosExercises_obj = VideosExercises(video_id = videoID, exercise_id = exerciseObj)
	videosExercises_obj.save()

def addTagsToDB(listOfTags, exerciseObj):
	"""addTagsToDB

	This subroutine calls createTag for each individual tag inside of the listOfTags.
	Args:
	listOfTags : List of tags in string format
	exerciseObj: An instance of the newly created exercise object from Create Exercise.

	Returns:
	Nothing

	"""
	for tag in listOfTags:
		if not tag.strip() =='':
			createTag(tag.lstrip(), exerciseObj)

def createTag(tag, exerciseObj):
	"""createTag

	This subroutine inserts into the Tags table if the given tag(string) doesn't exist in the table already. It will then call TagsExercises with the new Tags object to form a normalized relatinship.
	If the tag already does exist, then it simply gets the pre-existing tag object and attaches it to the TagsExercises table to form a normalized relatinship.
	Args:
	tag: A given tag in string format
	exerciseObj: An instance of the newly created exercise object from Create Exercise.

	Returns:
	Nothing

	"""
	tag_obj = Tags()
	if not Tags.objects.filter(tagDescription=tag).exists():
		tag_obj = Tags(tagDescription = tag)
		tag_obj.save()
	else:
		tag_obj = Tags.objects.get(tagDescription=tag)

	createTagRelationship(tag_obj, exerciseObj)

def createTagRelationship(tag_obj, exerciseObj):
	"""createTagExerciseRelationship

	This subroutine creates a TagsExercises object (a normalized table used to store relationships of exercises to tags)
	Args:
	tag_obj : An instance of the Tag object.
	exerciseObj: An instance of the newly created exercise object from Create Exercise.

	Returns:
	Nothing

	"""
	tagRelationshipObj = TagsExercises(tag_id = tag_obj, exercise_id = exerciseObj)
	tagRelationshipObj.save()
