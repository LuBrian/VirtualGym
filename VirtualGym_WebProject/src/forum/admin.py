from django.contrib import admin

# Register your models here.
from .models import Questions

class QuestionsAdmin(admin.ModelAdmin):
    """
    Set up question and answer in back end admin page 
    """
    list_display=["questionID","questionDescription","userID","dateAsked"]
    search_fields=["dateAsked","questionDescription"]
    class Meta:
        model=Questions


admin.site.register(Questions,QuestionsAdmin)
