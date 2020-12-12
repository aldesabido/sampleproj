from django.db import models
from django.db.models import Count, Sum, Avg,Min,Q,F,Func
from ..views.common import *


class Test_class(models.Model):
	name = models.CharField(max_length=200)

	class Meta:
		app_label = "project"
		db_table  = "test_classes"

	def __str__(self):
		return self.name

class Department(models.Model):
	name = models.CharField(max_length=200)

	class Meta:
		app_label = "project"
		db_table  = "departments"

	def __str__(self):
		return self.name

class Activity(models.Model):
	name = models.CharField(max_length=200)

	class Meta:
		app_label = "project"
		db_table  = "activities"
		verbose_name_plural = "Activities"


	def __str__(self):
		return self.name

class TaskType(models.Model):
	name = models.CharField(max_length=200)

	class Meta:
		app_label = "project"
		db_table  = "tasktypes"

	def __str__(self):
		return self.name
		
	def as_dict(self):
		return {
			"id":self.pk,
			"name":self.name
		}

