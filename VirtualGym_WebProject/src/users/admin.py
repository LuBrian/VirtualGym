from django.contrib import admin
from django.utils.html import format_html
from .models import MyUsers

class UsersAdmin(admin.ModelAdmin):

    """
    Set up comment in back end admin page by managing which fields of the Exercise model are displayed, which actions you can select, and how it is filtered.
    """
    list_display=["username", "User_Status"]
    list_filter=["username"]
    search_fields=["username"]


    def change_view(self,request,object_id,extra_content=None):
        self.fields = ('email','username','last_login','is_active', 'is_admin', 'is_superuser')
	self.readonly_fields = ['username','last_login','_date_joined']
        return super(UsersAdmin,self).change_view(request,object_id)

    def User_Status(self, obj):
        return format_html('<Button><a href="/admin/users/myusers/{}/change/">Change Status</a></button> &nbsp', obj.user_id) + format_html('<Button><a href="/admin/users/myusers/{}/delete/">Delete</a></button></>', obj.user_id)
    class Meta:
        model=MyUsers

admin.site.register(MyUsers,UsersAdmin)
