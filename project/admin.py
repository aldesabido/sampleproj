from django.contrib import admin
from .models.settings import *
from .models.users import *

admin.site.register(User)
admin.site.register(Department)
admin.site.register(TaskType)
admin.site.register(Activity)
