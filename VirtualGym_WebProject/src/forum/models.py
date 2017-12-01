from django.db import models
from users.models import MyUsers
from django.core.urlresolvers import reverse


class Question(models.Model):
	"""
	Questions object database schema build

	@type  questionID: int
	@param questionID: The id of the Questions.
	@type  Description: string
	@param Description: the descriptin of question.
	@type  dateAsked: date and time
	@param dateAsked: time of question post.
	@type  Answer: string
	@param Answer: the descriptin of answer.
	"""
	questionID = models.AutoField(primary_key=True)
	Question = models.CharField(null = False, blank = False, max_length=1000)
	Answer=models.CharField(null = True, blank = False, max_length=1000)
	dateAsked = models.DateTimeField(auto_now_add=True)
	class Meta():
        #setting questiong showing order according date
		ordering=["-dateAsked"]

	def __str__(self):
		"""
        return poster name for each comment
		"""
		return self.Question

	def get_absolute_url(self):
		"""
		return the url of QA
		"""
		return reverse("QA")
