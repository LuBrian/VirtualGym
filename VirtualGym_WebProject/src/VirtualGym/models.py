from django.db import models
from users.models import MyUsers

#This is using normalization to represent a many to many relationship.
#A tag can be used by many different exerciseIDs.

class Questions(models.Model):
	questionID = models.AutoField(primary_key=True)
	questionDescription = models.CharField(max_length=1000)
	exerciseID = models.ForeignKey('Exercise', on_delete=models.CASCADE)
	userID = models.ForeignKey('MyUsers.user_id', on_delete=models.CASCADE)
	dateAsked = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):              # __unicode__ on Python 2
		return self.questionDescription
        
        
class VideosExercises(models.Model):
      video_id = models.ForeignKey('Videos.video_id')
      exercise_id = models.ForeignKey('Exercise.exerciseID')
      
class TagsExercises(models.Model):
	tag_id = models.ForeignKey('Tags.tagID')
	exercise_id = models.ForeignKey('Exercise.exerciseID')

class QuestionsExercises(models.Model):
	question_id = models.ForeignKey('Questions.questionID')
	exercise_id = models.ForeignKey('Exercise.exerciseID')

class Videos(models.Model):
	video_id = models.AutoField(primary_key=True)
	videoFile = models.FileField(null=False,max_length=500,upload_to='./uploadVideo/')
	
class Exercise(models.Model):
	exerciseID = models.AutoField(primary_key=True)
	exerciseDescription = models.CharField(db_index=True, max_length=500)
	exerciseTag = models.ManyToManyField('Tags', through=TagsExercises)
	exerciseQuestions = models.ManyToManyField('Questions', through=QuestionsExercises)
	exerciseData = models.DateTimeField(auto_now_add=True)
	exercisePosterId = models.ForeignKey('MyUsers.user_id')
	exerciseVideos = models.ManyToManyField('Videos', through=VideosExercises)
	exerciseApproved = models.BooleanField(default=False)
	def __str__(self):              # __unicode__ on Python 2
		return self.exerciseDescription
		

#This table stores all of the tags and their given text.
class Tags(models.Model):
	tagID = models.AutoField(primary_key=True)
	tagDescription = models.CharField(db_index=True, max_length=100, unique=True)
	
	def __str__(self):              # __unicode__ on Python 2
		return self.tagDescription
		
class Answers(models.Model):
	answerID = models.AutoField(primary_key=True)
	questionID = models.ForeignKey('Questions')
	answerDescription = models.CharField(max_length=1000)
	userID = models.ForeignKey('MyUsers.user_id', on_delete=models.CASCADE)
	dateAnswered = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):              # __unicode__ on Python 2
		return self.answerDescription
