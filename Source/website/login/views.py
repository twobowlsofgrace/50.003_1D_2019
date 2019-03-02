from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm

def index(request):
    #if request.user.is_authenticated:
    #    return HttpResponseRedirect('/home/')
    #else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
	    
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
	    
                if user is not None:
                    # login success
                    login(request, user)  # saves user's ID in the session
                    return HttpResponseRedirect('/home/')
            else:
     	        # login failure
                return render(request, 'login/not_logged_in.html', {'form':LoginForm()})


        elif request.method == 'GET':
            return render(request, 'login/not_logged_in.html', {'form':LoginForm()})

        return HttpResponse("/home/")
        #return render(request, 'login/login.html')

def log_out(request):
    logout(request)

    return render(request, 'login/not_logged_in.html', {'form':LoginForm()})

















