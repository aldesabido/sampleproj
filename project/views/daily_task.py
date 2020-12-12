from ..models.users import *
from ..models.daily_plan import *
from ..views.common import *
from pprint import pprint


def main_page(request):
	return render(request, 'daily_task/main_page.html',{"page_name": "Daily Tasks"})

def create_dialog(request):
	return render(request, 'daily_task/dialogs/create_dialog.html',)

def read_pagination(request):
	params = post_data(request)


	# params = date_range_filter(params)

	date_from = params.get("date_from",None)
	date_to = params.get("date_to",None)

	if not date_from or not date_to:
		return error("Please input the two dates.")



	date_from = date_str_to_date(date_from)
	date_to = date_str_to_date(date_to)


	name_search = params.get("name",None)





	numdays = (date_to - date_from).days + 1
	date_list = [date_to - idatetime.timedelta(days=x) for x in range(numdays)]

	user_instances = User.objects.filter(is_active = True).exclude(department = None)
	if name_search:
		filters = (Q(fullname__icontains=name_search) | Q(email__icontains=name_search))
		user_instances = user_instances.filter(filters)

	user_ids = list(user_instances.values_list("id", flat = True))


	for datee in sorted(date_list):
		formatted_date_key = str(datee)
		for user_instance in user_instances:
			instance = None
			if not DailyPlan.objects.filter(user = user_instance,date = formatted_date_key).exists():
				instance = DailyPlan.objects.create(**{
					"user": user_instance,
					"date": formatted_date_key
				})

	record_instances = DailyPlan.objects.filter(user__in = user_ids,) \
							.filter(date__gte = date_from, date__lte = date_to) \
							.order_by("user","date")

	results = {"data": []}
	for record_instance in record_instances:
		row = record_instance.as_dict()

		

		row["date"] = "%s (%s)"%(record_instance.date,record_instance.date.strftime("%a"))

		row.update({
			"no_tasks": 0,
			"no_targets": 0,
			"accomplished": 0,
		})

		results["data"].append(row)
		pprint(results)
	return success_list(results, False)

def search_user(request):
	post = post_data(request)
	if post:
		hello = "hello"
		pprint(hello)
	else:
		pprint('nothing')

	return hello
