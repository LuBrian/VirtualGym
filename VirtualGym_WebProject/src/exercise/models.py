from django.db import models

# Create your models here.

class Exercise(models.Model):
    create = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    votes = models.IntegerField(default=0)