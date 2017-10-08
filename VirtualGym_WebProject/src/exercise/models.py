from django.db import models
from users.models import SignUp
# Create your models here.

class Exercise(models.Model):
    exerciseId = models.AutoField(primary_key=True)
    exerciseDescription = models.CharField(max_length=500)
    exerciseTag = models.CharField(max_length=50,null=False)
    exerciseData = models.DateTimeField(auto_now_add=True,auto_now=False)
    exercisePosterId = models.ForeignKey(SignUp)

    def __str__(self):              # __unicode__ on Python 2
        return (self.exerciseDescription)

    #timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    # def __str__ (self):
    #     return str(self.user_name)
