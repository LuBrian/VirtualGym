from django.db import models
from users.models import MyUsers

# Create your models here.
class Questions(models.Model):
	questionID = models.AutoField(primary_key=True)
	questionDescription = models.CharField(null = False, blank = False, max_length=1000)
	# exerciseID = models.ForeignKey('Exercise', on_delete=models.CASCADE)
	userID = models.ForeignKey(MyUsers, on_delete=models.CASCADE)
	dateAsked = models.DateTimeField(auto_now_add=True)

	def __str__(self):              # __unicode__ on Python 2
		return self.questionDescription
