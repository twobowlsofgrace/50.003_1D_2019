from django.urls import reverse
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password

from .forms import LoginForm


error_message_incorrect_userpass = "Login failure, username or password is incorrect"

@csrf_exempt
def index(request):
	#if request.user.is_authenticated:
	#    return HttpResponseRedirect('/home/')
	#else:

	error_message = None
	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			print(User.objects.get(username=username).password)
			user = authenticate(username=username, password=password)
			if user is not None:
				# login success
				login(request, user)  # saves user's ID in the session
				return HttpResponseRedirect(reverse("home:index"))
			else:
				error_message = error_message_incorrect_userpass
		else:
			# login failure
			error_message = "Invalid input"


	elif request.method == 'GET':
		pass

	return render(request, 'login/not_logged_in.html', {'form':LoginForm(), 'error_message':error_message})

def log_out(request):
	error_message = None
	logout(request)
	return HttpResponseRedirect(reverse('login:index'))
















