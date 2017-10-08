from django.db import models

#This is using normalization to represent a many to many relationship.
#A tag can be used by many different exerciseIDs.

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
	videoFile = models.FileField(upload_to='uploads/videos')
	
# Create your models here.        
class User(models.Model):
	userID = models.AutoField(primary_key=True)
	userName = models.CharField(max_length=30)
	userType = models.CharField(max_length=10)
			
	def __str__(self):
		return userName
	
	#userPicture = ImageWithThumbsField(upload_to='images', sizes=((125,125),(215,215)),null=True)
	
class Exercise(models.Model):
	exerciseID = models.AutoField(primary_key=True)
	exerciseDescription = models.CharField(db_index=True, max_length=500)
	exerciseTags = models.ManyToManyField('Tags', through=TagsExercises)
	exerciseQuestions = models.ManyToManyField('Questions', through=QuestionsExercises)
	exerciseDateCreated= models.DateTimeField(auto_now_add=True)
	exerciseAuthor = models.ForeignKey('User')
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
		
class Questions(models.Model):
	questionID = models.AutoField(primary_key=True)
	questionDescription = models.CharField(max_length=1000)
	exerciseID = models.ForeignKey(Exercise, on_delete=models.CASCADE)
	userID = models.ForeignKey(User, on_delete=models.CASCADE)
	dateAsked = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):              # __unicode__ on Python 2
		return self.questionDescription
        
class Answers(models.Model):
	answerID = models.AutoField(primary_key=True)
	questionID = models.ForeignKey('Questions')
	answerDescription = models.CharField(max_length=1000)
	userID = models.ForeignKey(User, on_delete=models.CASCADE)
	dateAnswered = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):              # __unicode__ on Python 2
		return self.answerDescription
