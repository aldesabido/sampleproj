from ..models.users import *
from ..models.daily_plan import *
from ..models.settings import *
from ..views.common import *
from pprint import pprint


def main_page(request):

	return render(request, 'task_types/main_page.html',{"page_name": "Task Types"})

def create_dialog(request):
	return render(request, 'task_types/dialogs/create_dialog.html',)

def read_pagination(request):
	params = post_data(request)

	name_search = params.get('name',None)

	record_instances = TaskType.objects.all()
	if name_search:
		filters = (Q(name__icontains=name_search))
		record_instances = record_instances.filter(filters)

	results={"data":[]}
	for record_instance in record_instances:
		row = record_instance.as_dict()
		print(record_instance)
		
		results["data"].append(row)
	
	return success_list(results,False)

def delete_task(request):
	param = post_data(request)
	pprint(param)

	tasktype_instance = TaskType.objects.get(id=param)
	tasktype_instance.delete()

	return success("Successfuly Deleted")

def edit_task(request):
	param = post_data(request)
	record_instances = TaskType.objects.get(id=param)
	results={"data":[]}
	record_instances = record_instances.as_dict()
	results["data"].append(record_instances)

	return success_list(results,False)


def create(request):
	params = post_data(request)
	name =  params.get("name",None)
	tid = params.get("id",None)
	if tid:
		TaskType.objects.filter(id=tid).update(name=name)
		return success("Successfuly Editted!")
	else:
		instance = TaskType(name=name)
		instance.save()
		return success("Successfuly Added!")


	

	