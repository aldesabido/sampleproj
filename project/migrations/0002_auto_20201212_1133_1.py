# Generated by Django 2.2.16 on 2020-12-12 03:33

from django.db import migrations

from django.contrib.auth import hashers
def create_default_user(apps,schema_editor):
	User = apps.get_model("project","User")

	User.objects.all().delete()
	password = hashers.make_password("123123")

	data = {
		"email": "admin@gmail.com",
		"fullname": "Super Admin",
		"password": password,
		"is_active": True,
		"is_developer": True,
		"is_employee": False,
		"gender": "M"
	}

	instance = User.objects.create(**data)

class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
    	migrations.RunPython(create_default_user)
    ]
