from django.contrib import admin

# Register your models here.
from .models import Questions

class QuestionsAdmin(admin.ModelAdmin):
    """
    Set up question and answer in back end admin page
    """
    list_display=["questionID","Answer","Description","dateAsked"]
    search_fields=["dateAsked","Description"]
    list_filter=["dateAsked"]
    class Meta:
        model=Questions


admin.site.register(Questions,QuestionsAdmin)
