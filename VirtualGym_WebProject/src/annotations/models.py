# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from exercise.models import Videos

# Create your models here.
"""/******************************
** File: models.py 
** Desc: This file forms the relevant back-end database structure for MyUsers in the VirtualGym web application.
** The tables are viewed as "models" in Django and are viewed as "tables" in the database.
*******************************/"""

class Annotation(models.Model):
	"""
	Creates and saves a User with the given email, and password.
	"""

	"""
	Perform creat annotation on a video

	@type  AnnotationId: int
	@param AnnotationId: Auto generated annotation Id
	@type  toVid: int
	@param toVid: point to this annotation's video id
	@type  details: char
	@param details: json string describes the detaisl of this annotation
	"""

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
