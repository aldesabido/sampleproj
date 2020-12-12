from ..models.users import *
from ..views.common import *


def home(request):
	return render(request, 'reports/reports.html',{"page_name": "Reports"})