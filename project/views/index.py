from ..forms.users import *
from ..models.users import *
from ..views.common import *

from django.contrib.auth import authenticate, hashers, logout as logoutt, login as loginn
from django.contrib.auth.tokens import default_token_generator 
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode 


def landingpage(request):
	if not request.user.id:
		return redirect("loginpage")
		return render(request, 'home/landing_page.html')
	else:
		return redirect("home")

def landingpage2(request):
	return redirect("loginpage")
	if not request.user.id:
		return render(request, 'home_ecada/index.html')
	else:
		return redirect("home")

def loginpage(request):
	if not request.user.id:
		return render(request, 'home/login_page.html')
	else:
		return redirect("home")

def loginpage2(request):
	if not request.user.id:
		return render(request, 'home_ecada/login_page2.html')
	else:
		return redirect("home")

def registration_dialog(request):
	return render(request, 'home/dialogs/register.html')

def login(request):
	"""Javascript sends data here. The user is either then authenticated, asked to select a company or errors are returned."""
	if request.method == "POST":
		result = {}
		data = post_data(request)
		try:
			username = data.get('email',"")
			password = data.get('password',"")

			user = authenticate(username = username, password = password)

			if user:
				if not user.is_active or user.deleted:
					raise ValueError("This user is inactive. Kindly contact your admin at aldesabido@gmail.com")
				loginn(request, user)
				return success("Successfully logged in. Redirecting...")
			else:
				raise_error("Invalid username/password.")
		except Exception as e:
			return error(e)
	else:
		return redirect("loginpage")

def logout(request):
	request.session.clear()
	logoutt(request)
	return redirect("landingpage2")

def home(request):
	if request.method == "GET":
		return render(request, 'base.html')

def dashboard(request):
	if request.method == "GET":
		return render(request, 'home/dashboard.html')

def orders(request):
	if request.method == "GET":
		return render(request, 'orders/active.html')