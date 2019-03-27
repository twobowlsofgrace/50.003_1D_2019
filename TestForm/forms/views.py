from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import BasicForm
from input_field_test import Input_field_test

import urllib


error_message_success = "Form submitted!"
error_message_empty_input = "Please fill in all input fields"
error_message_invalid_input = "Please ensure input fields are valid"


def basic_form(request):
	error_message = None

	if request.method == 'POST':
		title_validity = []
		description_validity = []
		name_validity = []
		phonenumber_validity = []
		email_validity = []
		title = None
		description = None
		name = None
		phonenumber = None
		email = None

		form = BasicForm()

		try:
			title = request.POST.get('title')
			description = request.POST.get('description')
			name = request.POST.get('name')
			phonenumber = request.POST.get('phonenumber')
			email = request.POST.get('email')
		except ValueError:
			pass

		# testing input field validity
		input_field_test = Input_field_test()
		title_validity = input_field_test.ticket_title(title)
		description_validity = input_field_test.ticket_description(description)
		name_validity = input_field_test.username(name)
		phonenumber_validity = input_field_test.phonenumber(phonenumber)
		email_validity = input_field_test.email(email)

		if len(title_validity)==1 and len(description_validity)==1 and len(name_validity)==1 and len(phonenumber_validity)==1 and len(email_validity)==1:
			# input fields are valid
			error_message = error_message_success
		else:
			# input fields are not valid
			empty_input_state = False
			invalid_input_state = False

			for i in title_validity:
				if i == "empty":
					empty_input_state = True
				elif i == "invalid value":
					invalid_input_state = True
			for i in description_validity:
				if i == "empty":
					empty_input_state = True
				elif i == "invalid value":
					invalid_input_state = True
			for i in name_validity:
				if i == "empty":
					empty_input_state = True
				elif i == "invalid value":
					invalid_input_state = True
			for i in phonenumber_validity:
				if i == "empty":
					empty_input_state = True
				elif i == "invalid value":
					invalid_input_state = True
			for i in email_validity:
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

		return render(request, 'forms/index.html', {'form': form, 'error_message':error_message})
	else:
		form = BasicForm()
		print(urllib.request("127.0.0.1:3000/ticket_creation/remote_create", headers={'key int':1, 'key string':"sample string"}))
		return render(request, 'forms/index.html', {'form': form, 'error_message':error_message})
