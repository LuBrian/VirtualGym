from django.contrib import admin

# Register your models here.
from .models import Exercise

def approve_exercise(modeladmin, request, queryset):
    queryset.update(exerciseApproved=True)
approve_exercise.short_description = "Approve Selected Exercise"

def reject_exercise(modeladmin, request, queryset):
    queryset.delete()
reject_exercise.short_description = "Reject Selected Exercise"

class ExerciseAdmin(admin.ModelAdmin):        
    actions = [approve_exercise, reject_exercise]
    list_display=["exerciseId","exercisePosterId","exerciseDescription","exerciseData"]
    list_filter=["exerciseDescription"]
    search_fields=["exercisePosterId","exerciseTag"]

    def has_add_permission(self, request):
        return False
    
    def get_queryset(self, request):
        return super(ExerciseAdmin,self).get_queryset(request).filter(exerciseApproved=False)
    
    def get_actions(self, request):
        actions = super(ExerciseAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
    class Meta:
        model=Exercise


admin.site.register(Exercise,ExerciseAdmin)
