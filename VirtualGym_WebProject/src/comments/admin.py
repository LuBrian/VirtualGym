from django.contrib import admin

# Register your models here.
from .models import Comment

"""
Set up comment in back end admin page 
"""
admin.site.register(Comment)
