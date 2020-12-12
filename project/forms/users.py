from django import forms
from ..models.users import *
from ..models.settings import *


class Users_create_form(forms.ModelForm):
	class Meta:
		model = User
		fields = ('email','fullname','department','password')

class Users_create_form2(forms.ModelForm):
	class Meta:
		model = User
		fields = ('email','fullname','department','password')

class Users_edit_form(forms.ModelForm):
	class Meta:
		model = User
		fields = ('email','fullname','department','password')

class Users_change_password_form(forms.ModelForm):
	class Meta:
		model = User
		fields = ('password',)

class Users_login_form(forms.ModelForm):
	class Meta:
		model = User
		fields = ('email','password')



#Misc

class Department_form(forms.ModelForm):
	class Meta:
		model = Department
		fields = ('name',)

class TaskType_form(forms.ModelForm):
	class Meta:
		model = TaskType
		fields = ('name',)

class Activity_form(forms.ModelForm):
	class Meta:
		model = Activity
		fields = ('name',)