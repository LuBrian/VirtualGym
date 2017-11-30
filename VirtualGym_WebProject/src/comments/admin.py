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
    list_display=["CommentPoster","CommentContent"]
    list_filter=["CommentPoster"]
    search_fields=["CommentContent"]

    class Meta:
        model=Comment

admin.site.register(Comment,CommentsAdmin)