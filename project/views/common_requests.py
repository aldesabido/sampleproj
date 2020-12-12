from ..models.users import *
from ..models.settings import *
from ..views.common import *


# Common template
def pagination(request):
	return render(request, 'common/pagination.html')



