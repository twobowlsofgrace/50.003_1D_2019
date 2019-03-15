from django.urls import reverse
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password

from .forms import LoginForm


@csrf_exempt
def index(request):
    #if request.user.is_authenticated:
    #    return HttpResponseRedirect('/home/')
    #else:
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
                    return redirect("/home/")
                else:
                    print("Login failed")
            else:
     	        # login failure
                return render(request, 'login/not_logged_in.html', {'form':LoginForm()})


        elif request.method == 'GET':
            return render(request, 'login/not_logged_in.html', {'form':LoginForm()})

        #return HttpResponse("/home/")
        return render(request, 'login/not_logged_in.html')

def log_out(request):
    logout(request)

    return HttpResponseRedirect(reverse("login:index"))

















