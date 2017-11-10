# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from exercise.models import Videos

# Create your models here.


class Annotation(models.Model):
	AnnotationId = models.AutoField(primary_key = True)
	toVid = models.ForeignKey(Videos)
	details = models.CharField(null = False, blank = False, max_length=1000)
	class Meta():
		ordering = ["-AnnotationId"]

	def __str__(self):
		"""
        return poster name for each comment
		"""
		return self.details
