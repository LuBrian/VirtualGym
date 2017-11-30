from django.contrib import admin

from .models import MyUsers

class UsersAdmin(admin.ModelAdmin):

    """
    Set up comment in back end admin page by managing which fields of the Exercise model are displayed, which actions you can select, and how it is filtered.
    """
    list_display=["username"]
    list_filter=["username"]
    search_fields=["username"]

    class Meta:
        model=MyUsers

admin.site.register(MyUsers,UsersAdmin)
