from django.contrib import admin
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.html import format_html
from django.shortcuts import render, get_object_or_404, redirect
# Register your models here.
from .models import MyUsers
from .models import Exercise
from .models import Videos
from .models import VideosExercises
from .models import Tags
from .models import TagsExercises
from django.contrib import messages

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

    for exerciseID in exId:
        exerciseIDFinal = exerciseID['exerciseId']
        instance=get_object_or_404(Exercise,exerciseId=exerciseIDFinal)
        vid_instances = instance.exerciseVideos.all()
        for vids in vid_instances:
            vids.delete()

        videoEx = VideosExercises.objects.filter(exercise_id=exerciseIDFinal)
        videoEx.delete()

        tagEx = TagsExercises.objects.filter(exercise_id=exerciseIDFinal)
        for ex in tagEx:
            ex.delete()
    queryset.delete()


reject_exercise.short_description = "Reject Selected Exercise"


def reject_exerciseWithID(modeladmin, objectID):
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
    instance = get_object_or_404(Exercise, exerciseId=objectID)
    tag_instances = instance.exerciseTag.all()
    print(tag_instances)
    vid_instances = instance.exerciseVideos.all()
    for vid in vid_instances:
        vid.delete()

    videoEx = VideosExercises.objects.filter(exercise_id=objectID)

    for vidEx in videoEx:
        vidEx.delete()

    tagEx = TagsExercises.objects.filter(exercise_id=objectID)
    for ex in tagEx:
        ex.delete()

    tag_instances.delete()
    for tag in tag_instances:
        tag.delete()
    instance.delete()


reject_exercise.short_description = "Reject Selected Exercise"

from django.contrib.admin import SimpleListFilter

class TagFilter(SimpleListFilter):
    title = 'Tags' # or use _('country') for translated title
    parameter_name = 'Tags'

    def lookups(self, request, model_admin):
        tags = Tags.objects.filter(tagID__in = model_admin.model.objects.all().values_list('exerciseTag', flat = True).distinct())
        return [(c.tagID, c.tagDescription) for c in tags]


    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(exerciseTag__tagID__exact=self.value())

class ExerciseAdmin(admin.ModelAdmin):

    """
    Set up exercise in back end admin page by managing which fields of the Exercise model are displayed, which actions you can select, and how it is filtered.
    """
    actions = [approve_exercise, reject_exercise]
    list_display = ["exerciseName", "exerciseDate", "Tags",
                    "exerciseURL", "exerciseApproved", "Exercise_Status"]
    list_filter = ["exerciseApproved", TagFilter,]
    search_fields = ["exerciseTag__tagDescription",
                     "exercisePosterId__email", "exerciseName"]

    def exerciseURL(self, obj):
        """approve_exercise

    This subroutine is used to return the URL of the exercise in the admin panel.
        Args:
           obj : An instance of the exercise class


        Returns:
           a formatted string with a hardcoded server prefix attached to the suffix of the exercise instance's exerciseid.`

        """
        return format_html("<a target=_blank href='/{0}'>{0}</a>", obj.exerciseId)

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
        return super(ExerciseAdmin, self).get_queryset(request)

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

    def change_view(self,request,object_id,extra_content=None):
        self.fields = ('exerciseName','exerciseDescription','exercisePosterId','exerciseApproved')
        return super(ExerciseAdmin,self).change_view(request,object_id)

    def delete_view(self, request, object_id, extra_context=None):
        # if request.POST is set, the user already confirmed deletion
        if request.POST:
            instance = get_object_or_404(Exercise, exerciseId=object_id)
            reject_exerciseWithID(self, object_id)
            messages.success(request, 'Exercise {} was deleted'.format(instance.exerciseName))
            return redirect("/admin/exercise/exercise")
            # return super(ExerciseAdmin, self).delete_view(request, *args, **kwargs)
            # return reject_exercise(ExerciseAdmin, object_id, extra_context)

        return super(ExerciseAdmin, self).delete_view(request, object_id, extra_context)
        # reject_exercise(ExerciseAdmin, object_id, extra_context)

    def Exercise_Status(self, obj):
        return format_html('<Button><a href="/admin/exercise/exercise/{}/change/">Change Status</a></button> &nbsp', obj.exerciseId) + format_html('<Button><a href="/admin/exercise/exercise/{}/delete/">Delete</a></button></>', obj.exerciseId)

    class Meta:
        model = Exercise


admin.site.register(Exercise, ExerciseAdmin)
