# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Annotation

# Register your models here.
# set up annotation in admin page
admin.site.register(Annotation)