from django.db import models
from django.conf import settings

from exercise.models import Exercise

# Create your models here.
class Comment(models.Model):
    CommentPoster = models.ForeignKey(settings.AUTH_USER_MODEL,null=False,blank=True)
    CommentExercise=models.ForeignKey(Exercise)

    CommentContent=models.TextField()
    CommentTimestamp=models.DateTimeField(auto_now_add=True)
    # CommentParent=models.ForeignKey("self",null=True,blank=True)

    class Meta():
        ordering=["-CommentTimestamp"]


    def __str__(self):              # __unicode__ on Python 2
        # return "%s %s" %(self.exerciseDescription,self.exerciseVideos)
        ordering=["-CommentTimestamp"]
        return str(self.CommentPoster.username)
    # def children(self):
    #     return Comment.objects.filter(CommentParent=self)
    #
    # @property
    # def isParent(self):
    #     if self.CommentParent is not None:
    #         return False
    #     return True
