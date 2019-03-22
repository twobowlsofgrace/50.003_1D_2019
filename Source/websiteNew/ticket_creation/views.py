from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse

from . import models
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from input_field_test import Input_field_test

# code not verified


error_message = None
error_message_forbidden_administrator = "This feature is not available to administrators"
error_message_forbidden_nonadministrator = "This feature is not available to non-administrators"



@csrf_exempt
def create(request):
	if (request.user.is_authenticated):
		# user is logged in
		if not (request.user.is_superuser):
			# user is normal user
			if request.method == 'POST':
				username_validity = []
				title_validity = []
				email_validity = []
				description_validity = []
				id_validity = []
				username = None
				title = None
				email = None
				description = None
				id = None

				try:
					id = 5
					username = request.POST.get("username")
					title = request.POST.get("title")
					email = request.POST.get('email')
					description = request.POST.get('description')
				except ValueError:
					pass

				# testing input field validity
				input_field_test = Input_field_test()
				username_validity = input_field_test.username(username)
				title_validity = input_field_test.ticket_title(title)
				email_validity = input_field_test.email(email)
				description_validity = input_field_test.ticket_description(description)
				id_validity = input_field_test.ticket_id(id)

				if len(username_validity)==1 and len(title_validity)==1 and len(email_validity)==1 and len(description_validity)==1 and len(id_validity)==1:
					# input fields are valid
					ticket = models.Ticket(ticket_id=id, title=title, resolved=0, read=0, description=description, user=username)
					ticket.save()
					messages.add_message(request, messages.SUCCESS, 'Create Successful')
					return render(request, 'ticketcreation/creation.html', {'error_message':error_message})
				else:
					# input fields are not valid
					for i in username_validity:
		                                if i == "empty":
		                                        empty_input_state = True
		                                elif i == "invalid value":
		                                        invalid_input_state = True
		                        for i in title_validity:
		                                if i == "empty":
		                                        empty_input_state = True
		                                elif i == "invalid value":
		                                        invalid_input_state = True
		                        for i in email_validity:
		                                if i == "empty":
		                                        empty_input_state = True
		                                elif i == "invalid value":
		                                        invalid_input_state = True
		                        for i in description_validity:
		                                if i == "empty":
		                                        empty_input_state = True
		                                elif i == "invalid value":
		                                        invalid_input_state = True
		                        for i in id_validity:
		                                if i == "empty":
		                                        empty_input_state = True
		                                elif i == "invalid value":
		                                        invalid_input_state = True

		                        if empty_input_state:
		                                # input fields are empty
		                                error_message = error_message_empty_input
		                        elif invalid_input_state:
		                                # input fields have invalid input
		                                error_message = error_message_invalid_input

				return render(request, 'ticketcreation/creation.html', {'error_message':error_message})

		else:
			# user is superuser
			return HttpResponseForbidden(error_message_forbidden_administrator)
	else:
		return HttpResponseRedirect(reverse("login:index"))


def list(request):
	if (request.user.is_authenticated):
		# user is logged in
		if (request.user.is_superuser):
			# user is superuser
			list = models.Ticket.objects.all()
			return render(request, 'ticketcreation/show.html', {"list": list, 'error_message':error_message})
		else:
			# user is normal user
			return HttpResponseForbidden(error_message_forbidden_nonadministrator)
	else:
		# user is not logged in
		return HttpResponseRedirect(reverse("login:index"))


def detail(request):
	if (request.user.is_authenticated):
		# user is loggged in
		if (request.user.is_superuser):
			# user is superuser
			id = request.GET.get("id")
			try:
				models.Ticket.objects.filter(id=id).update(read=1)
				item = models.Ticket.objects.all().filter(id=id)
			except:
				raise HttpResponse(0)
			return render(request, 'ticketcreation/detail.html', {"item": item[0], 'error_message':error_message})
		else:
			# user is normal user
			return HttpResponseRedirect(reverse("home:index"))
	else:
		# user is not logged in
		return HttpResponseRedirect(reverse("login:index"))

def delete(request):
	if (request.user.is_authenticated):
		# user is logged in
		if (request.user.is_superuser):
			# user is superuser
			column_id = request.GET.get("id")
			print(column_id)
			line = models.Ticket.objects.filter(id=column_id).delete()
			list = models.Ticket.objects.all()
			return render(request, 'ticketcreation/show.html', {"list": list, 'error_message':error_message})
		else:
			# user is normal user
			return HttpResponseRedirect(reverse("home:index"))
	else:
		# user is not logged in
		return HttpResponseRedirect(reverse("login:index"))

