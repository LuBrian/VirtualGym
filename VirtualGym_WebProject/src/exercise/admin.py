from django.contrib import admin

# Register your models here.
from .models import Exercise
class ExerciseAdmin(admin.ModelAdmin):
    list_display=["exerciseId","exercisePosterId","exerciseDescription","exerciseTag","exerciseData"]
    search_fields=["exercisePosterId","exerciseTag"]
    class Meta:
        model=Exercise


admin.site.register(Exercise,ExerciseAdmin)
