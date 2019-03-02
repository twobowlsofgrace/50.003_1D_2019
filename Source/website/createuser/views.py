from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from .forms import UserForm

def get_user(request):
    if request.method == 'POST':

        form = UserForm(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            id = request.POST['id']
            email = request.POST['email']
            phoneNumber = request.POST['phoneNumber']

            user = User.objects.create_user(username, email, password)
            user.save()

            return HttpResponseRedirect('/login/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'createuser/user.html', {'form': form})
