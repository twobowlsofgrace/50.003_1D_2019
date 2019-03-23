from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from .forms import UserForm
from django.contrib import messages


@csrf_exempt
def get_user(request):
	#messages.add_message(request, messages.ERROR, 'User Exist!')
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		email = request.POST.get('email')
		phoneNumber = request.POST.get('phoneNumber')
		#if UserForm.is_valid(request.POST):
		user=User.objects.filter(username=username)
		if user.exists() == False:
			user = User.objects.create_user(username=username, email=email, password=password, phoneNumber=phoneNumber)
			user.is_active = True
			user.save()
			return HttpResponseRedirect(reverse("login:index"))
		else:
			messages.error(request, 'User Exist!')
		# return HttpResponseRedirect(reverse("createuser:index"))
	# if a GET (or any other method) we'll create a blank form
	else:
		form = UserForm()

	return render(request, 'createuser/user.html')
