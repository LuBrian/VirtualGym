from django.db import models
from users.models import MyUsers
from django.core.urlresolvers import reverse


class Questions(models.Model):
	"""
	Questions object database schema build

	@type  questionID: int
	@param questionID: The id of the Questions.
	@type  userID: user object
	@param userID: The poster of the question.
	@type  questionDescription: string
	@param questionDescription: the descriptin of comment.
	@type  dateAsked: date and time
	@param dateAsked: time of question post.
	@type  questionParent: question object
	@param questionParent: question object as a parent of itself replay.
	"""
	questionID = models.AutoField(primary_key=True)
	questionDescription = models.CharField(null = False, blank = False, max_length=1000)
	userID = models.ForeignKey(MyUsers, on_delete=models.CASCADE)
	dateAsked = models.DateTimeField(auto_now_add=True)
	questionParent=models.ForeignKey("self",null=True,blank=True)

	def __str__(self):
		"""
        return poster name for each comment
		"""
		return self.questionDescription

	def get_absolute_url(self):
		"""
		return the url of QA
		"""
		return reverse("QA")

	def children(self):
		"""
        return reply objects for each question
        """
		return Questions.objects.filter(questionParent=self)

	@property
	def isParent(self):
		"""
        check comment it is parent or not
        """
		if self.questionParent is not None:
			return False
		return True
