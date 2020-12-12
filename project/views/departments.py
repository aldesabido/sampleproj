from ..models.users import *
from ..models.daily_plan import *
from ..views.common import *
from pprint import pprint


def main_page(request):
	return render(request, 'departments/main_page.html',{"page_name": "Departments"})


def read_pagination(request):
	pass