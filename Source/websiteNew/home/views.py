from audioop import reverse

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User

def home(request):
    if (request.user.is_authenticated):
        # user is logged in
        if (request.user.is_superuser):
            # user is superuser
            return render(request, 'home/index.html')
        else:
            # user is normal user
            return render(request, 'home/index.html')
    else:
        # user has not logged in, redirect to login page
        return HttpResponseRedirect(reverse('login:index'))
