from users.models import MyUsers
from django.db import models

# Create your models here.

def upload_location(instance,filename):
    return "%s/%s" %(instance.exercisePosterId,filename)

class TagsExercises(models.Model):
    tag_id = models.ForeignKey('Tags')
    exercise_id = models.ForeignKey('Exercise')

class Tags(models.Model):
    tagID = models.AutoField(primary_key=True)
    tagDescription = models.CharField(db_index=True, max_length=100, unique=True)
    def __str__(self):
        return self.tagDescription

class VideosExercises(models.Model):
    video_id = models.ForeignKey('Videos')
    exercise_id = models.ForeignKey('Exercise')

class Videos(models.Model):
    video_id = models.AutoField(primary_key=True)
    exercisePosterId = models.ForeignKey(MyUsers)
    videoFile = models.FileField(null=False,upload_to=upload_location)

class Exercise(models.Model):
    exerciseId = models.AutoField(primary_key=True)
    exerciseDescription = models.CharField(max_length=500)
    exerciseTag = models.ManyToManyField('Tags',through=TagsExercises)
    exerciseData = models.DateTimeField(auto_now_add=True,auto_now=False)
    exercisePosterId = models.ForeignKey(MyUsers)
    # exerciseVideos = models.FileField(upload_to=upload_location,
    #                 null=False,
    #                 blank=True)
    exerciseVideos = models.ManyToManyField('Videos', through=VideosExercises)
    exerciseApproved = models.BooleanField(default=False)


    def __str__(self):              # __unicode__ on Python 2
        # return "%s %s" %(self.exerciseDescription,self.exerciseVideos)
        ordering=["-exerciseData"]
        return (self.exerciseTag)


    #timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    # def __str__ (self):
    #     return str(self.user_name)
