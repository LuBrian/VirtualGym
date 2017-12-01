from django.contrib import admin
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.html import format_html
# Register your models here.
from .models import Comment

"""
Set up comment in back end admin page 
"""


class CommentsAdmin(admin.ModelAdmin):

    """
    Set up comment in back end admin page by managing which fields of the Exercise model are displayed, which actions you can select, and how it is filtered.
    """
    list_display=["Content","Poster","Exercise","Comment_Status"]
    list_filter=["CommentPoster"]
    search_fields=["CommentContent"]

    def Poster(self, obj):
	return obj.CommentPoster
    
    def Content(self, obj):
	return obj.CommentContent

    def Exercise(self, obj):
	return format_html('<a href="/{}/">{}</a>', obj.CommentExercise.exerciseId, obj.CommentExercise.exerciseName)

    def Comment_Status(self, obj):
        return format_html('<Button><a href="/admin/comments/comment/{}/change/">Change Status</a></button> &nbsp', obj.CommentId) + format_html('<Button><a href="/admin/comments/comment/{}/delete/">Delete</a></button></>', obj.CommentId)

    class Meta:
        model=Comment

admin.site.register(Comment,CommentsAdmin)
