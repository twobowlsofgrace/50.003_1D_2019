from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def home(request):
	error_message = None

	if (request.user.is_authenticated):
		# user is logged in
		if (request.user.is_superuser):
			# user is superuser
			pass
		else:
			# user is normal user
			pass

		return render(request, 'home/index.html', {'error_message':error_message})
	else:
		# user has not logged in, redirect to login page
		return HttpResponseRedirect(reverse('login:index'))
