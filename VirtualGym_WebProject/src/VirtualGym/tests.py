import datetime
from django.test import TestCase
import users.models as U
import exercise.models as E
import comments.models as C
import forum.models as F


# def userSetUp():
# 	U.MyUsers.objects.create(username = 'harrbra', is_admin = True, is_superuser = True, email = 'test1@test.ca')
# 	U.MyUsers.objects.create(username = 'harrbra2', email = 'test2@test.ca')

# def tagSetUp():
# 	E.Tags.objects.create(tagDescription = 'weightlifting')
# 	E.Tags.objects.create(tagDescription = 'cardio')

# def tagExerciseSetUp():
# 	E.TagsExercises.objects.create(tag_id = E.Tags.objects.get(tagDescription = 'weightlifting'), 
# 		exercise_id = E.Exercise.objects.get(exerciseDescription = 'This is a deadlift.'))
# 	E.TagsExercises.objects.create(tag_id = E.Tags.objects.get(tagDescription = 'cardio'), 
# 		exercise_id = E.Exercise.objects.get(exerciseDescription = 'This is a deadlift.'))

# def commentSetUp():
# 	harrbra = U.MyUsers.objects.get(username = 'harrbra')
# 	C.Comment.objects.create(CommentPoster = harrbra, CommentContent ='How do I deadlift', 
# 		CommentExercise =E.Exercise.objects.get(exerciseDescription = 'This is a deadlift.'))


# def commentExercisesSetUp():
# 	QuestionsExercises.objects.create(question_id = Questions.objects.get(questionDescription = 'How do I deadlift?'), exercise_id = Exercise.objects.get(exerciseDescription = 'This is a deadlift.'))
# 	QuestionsExercises.objects.create(question_id = Questions.objects.get(questionDescription = 'How do I deadlift without pain in my back?'), exercise_id = Exercise.objects.get(exerciseDescription = 'This is a deadlift.'))

	

# def QASetUp():
# 	harrbra = U.MyUsers.objects.get(username = 'harrbra')
# 	F.Questions.objects.create(userID = harrbra, 
# 		questionID = '1', questionDescription = "QA_Description1")

# class UsersTestCase(TestCase):
# 	def setUp(self):
# 		userSetUp()
# 	def test_users_can_create(self):
# 		harrbra = U.MyUsers.objects.get(username = 'harrbra')
# 		self.assertEqual(harrbra.username, 'harrbra')
# 		harrbra2 = U.MyUsers.objects.get(username = 'harrbra2')

# 		self.assertEqual(harrbra.is_superuser, True)
# 		self.assertEqual(harrbra2.user_id, 2)
# 		self.assertEqual(harrbra2.is_superuser, False)
		
	
# class ExerciseTestCase(TestCase):
# 	def setUp(self):
# 		userSetUp()
# 		tagSetUp()		
		
# 		E.Exercise.objects.create(exerciseDescription = 'This is a deadlift.', 
# 			exercisePosterId = U.MyUsers.objects.get(username = 'harrbra'))
# 		tagExerciseSetUp()
# 		commentSetUp()
# 		#commentExercisesSetUp()
# 	def test_exercise_tester(self):
# 		currentMonth = datetime.datetime.today().month
# 		exercise = E.Exercise.objects.get(exerciseDescription = 'This is a deadlift.')
# 		exerciseTags = str(exercise.exerciseTag.all())

		

# 		self.assertEqual(exercise.exercisePosterId.email, 'test1@test.ca')
# 		self.assertEqual(exercise.exerciseApproved, False)
# 		self.assertNotEqual(exercise.exerciseData.month, currentMonth-1)




# 	def test_exercise_questions(self):
# 		exercise = E.Exercise.objects.get(exerciseDescription = 'This is a deadlift.')
# 		exerciseQuestions = str(exercise.comment_set.all())

# 		self.assertEqual('harrbra' in exerciseQuestions, True)



# class QATestCase(TestCase):
# 	"""Tests that Questions and Answers portion works"""
# 	def setUp(self):
# 		userSetUp()
# 		QASetUp()

		
# 	def test_QA(self):
# 		harrbra = U.MyUsers.objects.get(username = 'harrbra')
# 		question = F.Questions.objects.get(questionDescription="QA_Description1")
# 		self.assertEqual('test1@test.ca' in str(question.userID), True)