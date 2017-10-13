from django.db import models
from users.models import MyUsers
# Create your models here.

class VideosExercises(models.Model):
      video_id = models.ForeignKey('Videos')
      exercise_id = models.ForeignKey('Exercise')
      
class TagsExercises(models.Model):
	tag_id = models.ForeignKey('Tags')
	exercise_id = models.ForeignKey('Exercise')

class QuestionsExercises(models.Model):
	question_id = models.ForeignKey('Questions')
	exercise_id = models.ForeignKey('Exercise')

class Videos(models.Model):
	video_id = models.AutoField(primary_key=True)
	videoFile = models.FileField(null=False,max_length=500,upload_to='./uploadVideo/')
	videoPerspective = models.IntegerField(default=0)
#This table stores all of the tags and their given text.
class Tags(models.Model):
	tagID = models.AutoField(primary_key=True)
	tagDescription = models.CharField(db_index=True, max_length=100, unique=True)
	
	def __str__(self):              # __unicode__ on Python 2
		return self.tagDescription
		
class Questions(models.Model):
	questionID = models.AutoField(primary_key=True)
	questionDescription = models.CharField(max_length=1000)
	exerciseID = models.ForeignKey('Exercise', on_delete=models.CASCADE)
	userID = models.ForeignKey(MyUsers, on_delete=models.CASCADE)
	dateAsked = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):              # __unicode__ on Python 2
		return self.questionDescription
        
class Answers(models.Model):
	answerID = models.AutoField(primary_key=True)
	questionID = models.ForeignKey('Questions')
	answerDescription = models.CharField(max_length=1000)
	userID = models.ForeignKey(MyUsers, on_delete=models.CASCADE)
	dateAnswered = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):              # __unicode__ on Python 2
		return self.answerDescription
	
class Exercise(models.Model):
    exerciseId = models.AutoField(primary_key=True)
    exerciseDescription = models.CharField(max_length=500)
    exerciseTag = models.ManyToManyField('Tags', through=TagsExercises)
    exerciseData = models.DateTimeField(auto_now_add=True,auto_now=False)
    exercisePosterId = models.ForeignKey(MyUsers)
    exerciseVideos = models.ManyToManyField('Videos', through=VideosExercises)
    exerciseApproved = models.BooleanField(default=False)
    exerciseQuestions = models.ManyToManyField('Questions', through=QuestionsExercises)
    
    def __str__(self):              # __unicode__ on Python 2
        # return "%s %s" %(self.exerciseDescription,self.exerciseVideos)
        return (self.exerciseDescription)
    

    #timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    # def __str__ (self):
#     return str(self.user_name)
