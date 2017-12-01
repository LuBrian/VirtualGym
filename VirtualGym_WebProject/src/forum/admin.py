from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import Question

class QuestionsAdmin(admin.ModelAdmin):
    """
    Set up question and answer in back end admin page
    """
    list_display=["Question","Answer","dateAsked", "Question_Status"]
    search_fields=["dateAsked","Description"]
    list_filter=["dateAsked"]

    def Question_Status(self, obj):
        return format_html('<Button><a href="/admin/forum/question/{}/change/">Change Status</a></button> &nbsp', obj.questionID) + format_html('<Button><a href="/admin/forum/question/{}/delete/">Delete</a></button></>', obj.questionID)
    class Meta:
        model=Question

admin.site.register(Question,QuestionsAdmin)
