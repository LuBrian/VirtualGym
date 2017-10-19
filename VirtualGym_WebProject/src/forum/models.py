from django.db import models
from users.models import MyUsers
from django.core.urlresolvers import reverse

# Create your models here.
class Questions(models.Model):
	questionID = models.AutoField(primary_key=True)
	questionDescription = models.CharField(max_length=1000)
	# exerciseID = models.ForeignKey('Exercise', on_delete=models.CASCADE)
	userID = models.ForeignKey(MyUsers, on_delete=models.CASCADE)
	dateAsked = models.DateTimeField(auto_now_add=True)
	questionParent=models.ForeignKey("self",null=True,blank=True)

	def __str__(self):              # __unicode__ on Python 2
		return self.questionDescription

	def get_absolute_url(self):
		return reverse("QA")
	def children(self):
	    return Questions.objects.filter(questionParent=self)

	@property
	def isParent(self):
	    if self.questionParent is not None:
	        return False
	    return True
