'''from django.test import TestCase
from VirtualGym.models import User
import forum.models as QA
import users.models


def userSetUp():
	User.objects.create(userName = 'harrbra', userType = 'moderator')
	User.objects.create(userName = 'harrbra2', userType = 'physiotherapist')
	User.objects.create(userName = 'harrbra3', userType = 'exerciser')

def QASetUp():
	harrbra = User.objects.get(userName = 'harrbra')
	QA.Questions.objects.create(userID = harrbra, 
		questionID = '1', questionDescription = "QA_Description1")


# Create your tests here.
class QATestCase(TestCase):
	"""Tests that Questions and Answers portion works"""
	def setUp(self):
		userSetUp()
		QASetUp()
		harrbra = User.objects.get(userName = 'harrbra')
		
	def test_QA(self):
		harrbra = User.objects.get(userName = 'harrbra')
		self.assertEqual(harrbra.userType, 'moderator')
'''

'''		question = Questions.objects.get(questionID='1')
		self.assertEqual('harrbra' in question.userName, True)'''