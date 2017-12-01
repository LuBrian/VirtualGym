from users.models import MyUsers
from django.db import models
from django.core.urlresolvers import reverse

"""/******************************
** File: models.py
** Desc: This file forms the relevant back-end database structure for exercises in the VirtualGym web application.
** The tables are viewed as "models" in Django and are viewed as "tables" in the database.
*******************************/"""

def upload_location(instance,filename):
    return "%s/%s" %(instance.exercisePosterId,filename)

class TagsExercises(models.Model):
    """
    relation table about exercise and tag

    @type  exercise_id: int
    @param exercise_id: The id of the exercise.
    @type  tag_id: int
    @param tag_id: The id of tag.
    """
    tag_id = models.ForeignKey('Tags')
    exercise_id = models.ForeignKey('Exercise')

class Tags(models.Model):
    """
    tag object database schema build

    @type  tagDescription: string
    @param tagDescription: text of tags.
    @type  tagID: int
    @param tagID: The id of tag.
    """
    tagID = models.AutoField(primary_key=True)
    tagDescription = models.CharField(db_index=True, max_length=100, unique=True)
    def __str__(self):
        return str(self.tagDescription)

class VideosExercises(models.Model):
    """
    relation table about exercise and video

    @type  exercise_id: int
    @param exercise_id: The id of the exercise.
    @type  video_id: int
    @param video_id: The id of video.
    """
    video_id = models.ForeignKey('Videos')
    exercise_id = models.ForeignKey('Exercise')

class Videos(models.Model):
    """
    video object database schema build

    @type  exercisePosterId: user object
    @param exercisePosterId: video poster.
    @type  video_id: int
    @param video_id: The id of video.
    @type  exerciseVideos: video
    @param exerciseVideos: video of exercise.
    """
    video_id = models.AutoField(primary_key=True)
    exercisePosterId = models.ForeignKey(MyUsers)
    annotations = models.CharField(max_length=5000)
    videoFile = models.FileField(null=False,upload_to=upload_location)

# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

@receiver(pre_delete, sender=Videos)
def videos_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.videoFile.delete(False)

class Exercise(models.Model):
    """
    Exercise object database schema build

    @type  exerciseId: int
    @param exerciseId: The id of the exercise.
    @type  exercisePosterId: user object
    @param exercisePosterId: The poster of the question.
    @type  exerciseDescription: string
    @param exerciseDescription: the descriptin of question.
    @type  exerciseData: date and time
    @param exerciseData: time of exercise post.
    @type  exerciseTag: string
    @param exerciseTag: tag of exercise, could be more than one.
    @type  exerciseVideos: video
    @param exerciseVideos: video of exercise.
    @type  exerciseApproved: bool
    @param exerciseApproved: state of exercise, if true exercise will show in web.
    """
    exerciseId = models.AutoField(primary_key=True)
    exerciseDescription = models.CharField(max_length=5000)
    exerciseTag = models.ManyToManyField('Tags',through=TagsExercises)
    exerciseDate = models.DateTimeField(auto_now_add=True,auto_now=False)
    exercisePosterId = models.ForeignKey(MyUsers)
    exerciseVideos = models.ManyToManyField('Videos', through=VideosExercises)
    exerciseApproved = models.BooleanField(default=False)
    exerciseName = models.CharField(max_length=1000,blank = False)


    def __str__(self):
        """
        return  exercise Description
        """
        return str(self.exerciseDescription)

    def get_absolute_url(self):
        """
        return the url of each exercise according Id
        """
        return reverse("detail",kwargs={"id":self.exerciseId})
