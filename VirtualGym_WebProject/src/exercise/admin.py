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
"""/******************************
** File: admin.py
** Desc: This file is used to control the administration access used within the "exercises" submenu
** in the adminisration panel.
** Auth: Brad Harrison
** Date: Oct 19 2017
*******************************/"""

def approve_exercise(modeladmin, request, queryset):
    """approve_exercise

    This subrouine simply sets the exerciseApproved boolean to true wthin the exercise table of the db.
    It is a selectable action with the admin panel of exercise admin.
    Args:
        modeladmin (ExerciseAdmin): This is an instance of exerciseAdmin.
        request: This is unused but is relatd to the request connection.
        queryset: This is an instance of the given exercise model.

    Returns:
        nothing

    """
    queryset.update(exerciseApproved=True)
approve_exercise.short_description = "Approve Selected Exercise"

def reject_exercise(modeladmin, request, queryset):
    """reject_exercise

    This subrouine deletes the exercise and its dependents from the
    Video, VideoExercises, TagsExercises tables.
    It is a selectable action with the admin panel of exercise admin.
    Args:
        modeladmin (ExerciseAdmin): This is an instance of exerciseAdmin.
        request: This is unused but is relatd to the request connection.
        queryset: This is an instance of the given exercise model.

    Returns:
        nothing

    """
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
    Set up exercise in back end admin page by managing which fields of the Exercise model are displayed, which actions you can select, and how it is filtered.
    """
    actions = [approve_exercise, reject_exercise]
    list_display=["exercisePosterId","exerciseDescription","exerciseData","Tags", "exerciseURL", "Videos","exerciseApproved"]
    list_filter=["exerciseApproved","exerciseDescription"]
    search_fields=["exerciseTag__tagDescription","exercisePosterId__email","exerciseName"]


    def exerciseURL(self,obj):
        """approve_exercise

	This subroutine is used to return the URL of the exercise in the admin panel.
        Args:
           obj : An instance of the exercise class


        Returns:
           a formatted string with a hardcoded server prefix attached to the suffix of the exercise instance's exerciseid.`

        """
        return format_html("<a target=_blank href='http://127.0.0.1:8000/{0}'>{0}</a>", obj.exerciseId)

    def Tags(self, obj):
        """Tags

	This subroutine is used to return all Tags in the exercise object
        Args:
           obj : An instance of the exercise class


        Returns:
           a string of tags joined together per exercise.

        """
        return "\n".join([p.tagDescription for p in obj.exerciseTag.all()])

    def Videos(self, obj):
        """Videos

	This subroutine is used to return all Videos in the exercise object
        Args:
           obj : An instance of the exercise class


        Returns:
           a string of Videos joined together per exercise.

        """
        return "\n".join([static(p.videoFile.url) for p in obj.exerciseVideos.all()])

    def has_add_permission(self, request):
        """has_add_permission

	This subroutine manages whether or not we have the permission to create an exercise from the admin panel(we do not)
        Args:
           request : An instance of the exercise class


        Returns:
           False

        """
        return False

    def get_queryset(self, request):
        """get_queryset

	This subroutine returns a querset of the exercises to display in the admin panel.
        Args:
           request : An instance of the exercise class


        Returns:
           QuerySet of exercises to display in the admin panel

        """
        return super(ExerciseAdmin,self).get_queryset(request)

    def get_actions(self, request):
        """get_actions

	This subroutine returns a list of possible actions inside of the exercise admin panel
        Args:
           request : An instance of the exercise class


        Returns:
           A list of possible actions(it removes the default delete action)

        """
        actions = super(ExerciseAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
    class Meta:
        model=Exercise


admin.site.register(Exercise,ExerciseAdmin)
