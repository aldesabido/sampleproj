from ..models.settings import *
from ..models.users import *
from ..views.common import *


def default(request):
	return render(request, 'settings/settings.html',{"page_name": "Settings"})
