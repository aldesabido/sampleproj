
from django.conf.urls import url, handler404,include
from django.conf import settings as root_settings
from django.conf.urls.static import static

from project.views import (
		index,
		settings,
		common,
		common_requests,
		reports,
		daily_task,
		departments,
		task_types,
	)

urlpatterns = [
	url(r'^$', index.landingpage,name="landingpage"),
	url(r'^landingpage/$', index.landingpage2,name="landingpage2"),
	url(r'^login/$', index.loginpage,name="loginpage"),
	url(r'^login2/$', index.loginpage2,name="loginpage2"),
	url(r'^login/submit/$', index.login),
	url(r'^logout/$', index.logout),
	# url(r'^register/create_dialog/$', index.registration_dialog),
	# url(r'^register/$', index.register),


	url(r'^common/pagination/$', common_requests.pagination),



	url(r'^home/$', index.home,name="home"),
	url(r'^dashboard/$', index.dashboard),
	


	#Settings
	url(r'^daily_task/$', daily_task.main_page),
	url(r'^daily_task/read_pagination/$', daily_task.read_pagination),
	url(r'^daily_task/create_dialog/$', daily_task.create_dialog),
	url(r'^daily_task/search_user/$', daily_task.search_user),


	#Departments
	url(r'^departments/$', departments.main_page),
	url(r'^departments/read_pagination/$', departments.read_pagination),
	
	#Task Types
	url(r'^task_types/$', task_types.main_page),
	url(r'^task_types/read_pagination/$', task_types.read_pagination),
	url(r'^task_types/delete_task/$', task_types.delete_task),
	url(r'^task_types/edit_task/$', task_types.edit_task),
	url(r'^task_types/create_dialog/$', task_types.create_dialog),
	url(r'^task_types/create/$', task_types.create),





	#Settings
	url(r'^reports/$', reports.home),
]
# urlpatterns += static(root_settings.STATIC_URL,document_root=root_settings.STATIC_ROOT)
# urlpatterns += static(root_settings.MEDIA_URL,document_root=root_settings.MEDIA_ROOT)

# if root_settings.DEBUG:
#     import debug_toolbar
#     urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))