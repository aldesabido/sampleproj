from django import forms
from ..models.daily_plan import *


class DailyPlanForm(forms.ModelForm):
	class Meta:
		model = DailyPlan
		fields = (
			'user',
			'date',
		)


class DailyPlanDetailForm(forms.ModelForm):
	class Meta:
		model = DailyPlanDetail
		fields = (
			'dailyplan',
			'tasktype',
			'description',
			'qty_target',
			'qty_accomplished',
		)