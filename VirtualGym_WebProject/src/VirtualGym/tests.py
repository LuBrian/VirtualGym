import datetime
from django.test import TestCase
from VirtualGym.models import *

def userSetUp():
	User.objects.create(userName = 'harrbra', userType = 'moderator')
	User.objects.create(userName = 'harrbra2', userType = 'physiotherapist')
	User.objects.create(userName = 'harrbra3', userType = 'exerciser')

def tagSetUp():
	Tags.objects.create(tagDescription = 'weightlifting')
	Tags.objects.create(tagDescription = 'cardio')

def tagExerciseSetUp():
	TagsExercises.objects.create(tag_id = Tags.objects.get(tagDescription = 'weightlifting'), exercise_id = Exercise.objects.get(exerciseDescription = 'This is a deadlift.'))
	TagsExercises.objects.create(tag_id = Tags.objects.get(tagDescription = 'cardio'), exercise_id = Exercise.objects.get(exerciseDescription = 'This is a deadlift.'))

def questionsSetUp():
	Questions.objects.create(questionDescription = 'How do I deadlift?', exerciseID = Exercise.objects.get(exerciseDescription = 'This is a deadlift.'), userID = User.objects.get(userName = 'harrbra'))
	Questions.objects.create(questionDescription = 'How do I deadlift without pain in my back?', exerciseID = Exercise.objects.get(exerciseDescription = 'This is a deadlift.'), userID = User.objects.get(userName = 'harrbra'))

def questionExercisesSetUp():
	QuestionsExercises.objects.create(question_id = Questions.objects.get(questionDescription = 'How do I deadlift?'), exercise_id = Exercise.objects.get(exerciseDescription = 'This is a deadlift.'))
	QuestionsExercises.objects.create(question_id = Questions.objects.get(questionDescription = 'How do I deadlift without pain in my back?'), exercise_id = Exercise.objects.get(exerciseDescription = 'This is a deadlift.'))
	
class UsersTestCase(TestCase):
	def setUp(self):
		userSetUp()
	def test_users_can_create(self):
		harrbra = User.objects.get(userName = 'harrbra')
		harrbra2 = User.objects.get(userName = 'harrbra2')
		harrbra3 = User.objects.get(userName = 'harrbra3')
		self.assertEqual(harrbra.userType, 'moderator')
		self.assertEqual(harrbra2.userID, 2)
		self.assertEqual(harrbra3.userType, 'exerciser')
		

class ExerciseTestCase(TestCase):
	def setUp(self):
		userSetUp()
		tagSetUp()		
		
		Exercise.objects.create(exerciseDescription = 'This is a deadlift.', exerciseAuthor = User.objects.get(userName = 'harrbra'))
		tagExerciseSetUp()
		questionsSetUp()
		questionExercisesSetUp()
		
	def test_exercise_tester(self):
		exercise = Exercise.objects.get(exerciseDescription = 'This is a deadlift.')
		exerciseTags = str(exercise.exerciseTags.all())

		currentMonth = datetime.datetime.now().month
		self.assertEqual('weightlifting' in exerciseTags, True)
		self.assertEqual('cardio' in exerciseTags, True)
		self.assertNotEqual('bodyweight' in exerciseTags, True)
		

		self.assertEqual(exercise.exerciseAuthor.userName, 'harrbra')
		self.assertEqual(exercise.exerciseDateCreated.month, currentMonth)
		self.assertNotEqual(exercise.exerciseDateCreated.month, currentMonth-1)
		
	def test_exercise_questions(self):
		exercise = Exercise.objects.get(exerciseDescription = 'This is a deadlift.')
		exerciseQuestions = str(exercise.exerciseQuestions.all())
		
		self.assertEqual('How do I deadlift?' in exerciseQuestions, True)
		self.assertEqual('How do I deadlift without pain in my back?' in exerciseQuestions, True)
		self.assertNotEqual('How do I deadlift without pain in my leg?' in exerciseQuestions, True)
		
	
	
