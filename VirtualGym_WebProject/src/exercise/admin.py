from django.contrib import admin
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.html import format_html

# Register your models here.
from .models import Exercise
from .models import Videos
from .models import VideosExercises
from .models import Tags
from .models import TagsExercises

def approve_exercise(modeladmin, request, queryset):
    queryset.update(exerciseApproved=True)
approve_exercise.short_description = "Approve Selected Exercise"

def reject_exercise(modeladmin, request, queryset):
    exId = queryset.values("exerciseId")
    authId = queryset.values("exercisePosterId")
    videos = queryset.values("exerciseVideos")
    tags = queryset.values("exerciseTag")

    videoObj = Videos.objects.filter(video_id = videos)
    videoObj.delete()

    videoEx = VideosExercises.objects.filter(exercise_id = exId)
    videoEx.delete()

    tagEx = TagsExercises.objects.filter(exercise_id = exId, tag_id = tags)
    tagEx.delete()
    queryset.delete()


reject_exercise.short_description = "Reject Selected Exercise"

class ExerciseAdmin(admin.ModelAdmin):

    """
    Set up exercise in back end admin page
    """        
    actions = [approve_exercise, reject_exercise]
    list_display=["exercisePosterId","exerciseDescription","exerciseData","Tags", "exerciseURL", "Videos"]
    list_filter=["exerciseDescription"]
    search_fields=["exercisePosterId","exerciseTag"]

    def exerciseURL(self,obj):
    	return format_html("<a target=_blank href='http://127.0.0.1:8000/{0}'>{0}</a>", obj.exerciseId)

    def Tags(self, obj):
    	return "\n".join([p.tagDescription for p in obj.exerciseTag.all()])

    def getPath(self, obj):
    	return "test"

    def Videos(self, obj):
    	return "\n".join([static(p.videoFile.url) for p in obj.exerciseVideos.all()])

    def has_add_permission(self, request):
        return False

    def get_queryset(self, request):
        return super(ExerciseAdmin,self).get_queryset(request)

    def get_actions(self, request):
        actions = super(ExerciseAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
    class Meta:
        model=Exercise


admin.site.register(Exercise,ExerciseAdmin)
