from django.db import models
from ..views.common import *


class DailyPlan(models.Model):
	user = models.ForeignKey("User",on_delete=models.CASCADE)
	date = models.DateField()

	class Meta:
		app_label = "project"
		db_table  = "dailyplans"

	def __str__(self):
		return "%s - %s"%(self.user,self.date)

	def as_dict(self):
		row = model_to_dict(self,fields = ["id","date"])
		row["user"] = self.user.as_dict()
		return row


class DailyPlanDetail(models.Model):

	dailyplan = models.ForeignKey("DailyPlan",on_delete=models.CASCADE)
	tasktype = models.ForeignKey("TaskType",on_delete=models.CASCADE)
	description = models.TextField()
	qty_target = models.IntegerField()
	qty_accomplished = models.IntegerField()


	class Meta:
		app_label = "project"
		db_table  = "dailyplandetails"

	def __str__(self):
		return "%s - %s"%(self.dailyplan,self.description)


