from django.http import HttpResponse
from django.shortcuts import render
from . import models
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages



@csrf_exempt
def create(request):
    if request.method == 'POST':
        id = 5
        username = request.POST.get("username")
        title = request.POST.get("title")
        print(username)
        email = request.POST.get('email')
        description = request.POST.get('description')
        print(username)
        ticket = models.Ticket(ticket_id=id, title=title, resolved=0, read=0, description=description, user=username)
        ticket.save()
        messages.add_message(request, messages.SUCCESS, 'Create Successful')
    return render(request, 'ticketcreation/creation.html')


def list(request):
    list = models.Ticket.objects.all()

    return render(request, 'ticketcreation/show.html', {"list": list})


def viewit(request, id):
    item = models.Ticket.objects.all().filter(id = id)
    return render(request, 'ticketcreation/display.html',{"item":item[0]})

def delete(request):
    column_id = request.POST['column_id']
    print(column_id)
    try:
        line = models.Ticket.objects.filter(id == column_id).delete()
        line.save()
        return HttpResponse(1)
    except:
        return HttpResponse(0)

