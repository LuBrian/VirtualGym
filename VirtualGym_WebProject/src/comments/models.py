from django.db import models
from django.conf import settings

from exercise.models import Exercise


class Comment(models.Model):
    """
    Comment object database schema build

    @type  CommentId: int
    @param CommentId: The id of the comment.
    @type  CommentPoster: user object
    @param CommentPoster: The poster of the comment.
    @type  CommentExercise: exercise object
    @param CommentExercise: a exercise of comment.
    @type  CommentContent: string
    @param CommentContent: The descriptin of the comment.
    @type  CommentTimestamp: date and time
    @param CommentTimestamp: time of comment.
    @type  CommentParent: comment object
    @param CommentParent: comment object as a parent of itself replay.
    """
    CommentId=models.AutoField(primary_key=True)
    CommentPoster = models.ForeignKey(settings.AUTH_USER_MODEL,null=False,blank=True)
    CommentExercise=models.ForeignKey(Exercise)
    CommentContent=models.TextField()
    CommentTimestamp=models.DateTimeField(auto_now_add=True)
    CommentParent=models.ForeignKey("self",null=True,blank=True)


    class Meta():
        #setting comment showing order
        ordering=["-CommentTimestamp"]


    def __str__(self):
        """
        return poster name for each comment
        """
        ordering=["-CommentTimestamp"]
        return str(self.CommentPoster.username)

    def children(self):
        """
        return reply objects for each comment
        """
        return Comment.objects.filter(CommentParent=self)

    @property
    def isParent(self):
        """
        check comment it is parent or not
        """
        if self.CommentParent is not None:
            return False
        return True
